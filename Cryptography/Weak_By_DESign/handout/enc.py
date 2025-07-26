from Crypto.Cipher import DES
from Crypto.Util.Padding import pad

FLAG = "REDACTED for obvious reasons.. haha"
key = bytes.fromhex("66616b652d636174")

def encrypt(key, plaintext):
    cipher = DES.new(key, DES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), 8))
    return ciphertext.hex()

print(encrypt(key, FLAG))