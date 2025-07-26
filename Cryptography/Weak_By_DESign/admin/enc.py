from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

FLAG = "cyberQuest{D0_y0U_L0v3_w34K_k3y5_b25bb0f4284a57d3c56bc1c0ebd70084}"
key = bytes.fromhex("E0E0E0E0F1F1F1F1")

def encrypt(key, plaintext):
    cipher = DES.new(key, DES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), 8))
    return ciphertext.hex()

print(encrypt(key, FLAG))