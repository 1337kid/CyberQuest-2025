FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    procps \
    coreutils \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN groupadd -r appuser && useradd -r -g appuser -s /bin/false -c "Application User" appuser

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY .env .

COPY templates/ templates/
COPY flag.txt /flag.txt
RUN chmod 644 /flag.txt

RUN chown -R appuser:appuser /app

USER appuser

EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_ENV=production

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "app:app"] 