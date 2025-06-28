from flask import Flask, render_template, request, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import subprocess
import jwt
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('APP_SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

class Confession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

#with app.app_context():
#    db.create_all()

@app.route('/')
def index():
    confessions = Confession.query.all()
    return render_template('home.html', confessions=confessions)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            session['user_id'] = user.id
            flash('Login successful!', 'success')
            return redirect('/')
        else:
            flash('Invalid credentials', 'danger')
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'danger')
        else:
            new_user = User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully!', 'success')
            return redirect('/login')
    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Logged out successfully', 'success')
    return redirect('/login')

@app.route('/add_confession', methods=['POST'])
def add_confession():
    if 'user_id' not in session:
        return redirect('/login')

    content = request.form['content']
    user_id = session['user_id']
    new_confession = Confession(content=content, user_id=user_id)
    db.session.add(new_confession)
    db.session.commit()
    flash('Confession added!', 'success')
    return redirect('/')

@app.route('/serveruptimeforadmins', methods=['GET'])
def vulnerable():
    token = request.headers.get('Authorization')

    if not token:
        return "...... ??", 401

    try:
        jwt.decode(token, os.getenv('JWT_SECRET'), algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return "Token has expired", 401
    except jwt.InvalidTokenError:
        return "Invalid token", 401

    param = request.args.get('check', 'uptime')

    try:
        result = subprocess.check_output(param, shell=True, text=True)
        return f"<pre>Health Check Result:\n{result}</pre>", 200
    except subprocess.CalledProcessError as e:
        return f"Command failed: {e}", 400

@app.route("/healthcheck")
def healthcheck():
    return "ok", 200
