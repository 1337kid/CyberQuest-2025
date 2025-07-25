# 🧠 Solution: **Handling Binary File**

## 🔍 Challenge Overview

You’re given a binary file named `number_guessing` with very little context, other than a simple challenge description:

> **“You’ve intercepted a binary file named number\_guessing during a routine investigation of a compromised Linux machine. Handle with care.”**

This hints at classic **binary forensics**, and the filename suggests it might be some sort of **guessing game** — but the real goal is to uncover a hidden flag.

---

## 🛠️ Step 1: Run the Binary

Let’s start by executing the binary to see what it does:

```bash
chmod +x number_guessing
./number_guessing
```

You're prompted with:

```
🔐 Welcome to the Guessing Game!
Guess a number between 1 and 10:
```

It’s a basic number guessing game — harmless on the surface. But when you guess correctly, it prints:

```
✅ Correct! Here's a clue: The flag is hidden in this binary. Try using 'strings' with it.
```

That’s your real lead.

---

## 🔍 Step 2: Inspect the Binary with `strings`

Since the flag isn’t printed during execution, the next step is to **analyze the binary statically** using the `strings` utility:

```bash
strings number_guessing | grep -E '[A-Za-z0-9+/=]{20,}'
```

This reveals a suspicious-looking base64 string:

```
Y3liZXJRdWVzdHt5MHVfNjA3XzE3LHIwMGsxMyFfN2JmMGE3NzM3Y2I3YTlmYTcxNWUyMWJlNWMzMTRjYzF9
```

---

## 🔐 Step 3: Decode the Base64

Let’s decode it:

```bash
echo "Y3liZXJRdWVzdHt5MHVfNjA3XzE3LHIwMGsxMyFfN2JmMGE3NzM3Y2I3YTlmYTcxNWUyMWJlNWMzMTRjYzF9" | base64 -d
```

Output:

```
cyberQuest{y0u_607_17,r00k13!_7bf0a7737cb7a9fa715e21be5c314cc1}
```

---

## 🏁 Final Flag

```
cyberQuest{y0u_607_17,r00k13!_7bf0a7737cb7a9fa715e21be5c314cc1}
```

---