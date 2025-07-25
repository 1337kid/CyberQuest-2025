Here's the markdown-format walkthrough for **"The Whispering Cipher"** challenge, following the style you've provided:

---

# Solution: The Whispering Cipher 🕵️‍♂️🔐

## Challenge Overview

You're given an encrypted string and a series of hints that point to classic cryptographic techniques:

> "To unravel the whistleblower's note, you must listen closely to the whispers of cryptographic history."

The goal is to peel back each "layer" of the cipher using the hints provided.

---

## Step 1: Look at the Handout 📄

You're given the following encoded text:

```text
ZWdxbHZId21oYXszYnQzbl8yMDI1X0BfdTNyCl9taXY1Y2xwNDIzMW03Z3JjMjA3anU2bDg3aDc5MXM1OX0=
```

This looks suspiciously like Base64 due to the ending `=` padding and the character set.

---

## Step 2: Decode the Base64 Layer 🧬

Hint 1 tells us:

> "The first layer is a common text encoding method, often marked by = symbols at the end."

That screams **Base64**.

Run it through any Base64 decoder (e.g., `base64 -d`, CyberChef, or Python):

```bash
echo "ZWdxbHZId21oYXszYnQzbl8yMDI1X0BfdTNyCl9taXY1Y2xwNDIzMW03Z3JjMjA3anU2bDg3aDc5MXM1OX0=" | base64 -d
```

✅ Output:

```text
eqqlvHwmha{3bt3n_2025_@_u3r
_miv5clp4231m7grc207ju6l87h791s59}
```

We now have what **looks like a flag**, but it's still scrambled. The structure hints at a possible further cipher.

---

## Step 3: Apply the Classic Cipher 🔁

Hint 2:

> "Look for a historic cipher that uses a repeating keyword to create multiple letter shifts."

That clearly points to the **Vigenère cipher**.

---

## Step 4: Find the Keyword 🔑

Hint 3:

> "The secret keyword is a common term in the world of cryptography; think about the very subject of the puzzle."

Try decrypting the Base64-decoded string using **Vigenère cipher**, with:

* **Ciphertext**:

  ```
  eqqlvHwmha{3bt3n_2025_@_u3r_miv5clp4231m7grc207ju6l87h791s59}
  ```

* **Key**:

  ```
  cipher
  ```

You can use an online Vigenère decoder available in cyberchef.

---

## Step 5: Decrypted Flag Found 🎉

Decryption gives you:

```text
cyberQuest{3xc3l_2025_@_m3c_fee5ada4231f7caa207bf6e87d791b59}
```