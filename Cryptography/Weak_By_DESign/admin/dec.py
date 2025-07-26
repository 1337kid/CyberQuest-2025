from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

ciphertext = "b25431b1548dc978182bfd9249d5c6fb2e2d1b740b1a30901fe78a9b0527449c380ad4fd9ce798a0d0a57fe924827325b45c9d0905ddcf69b7074babf61ffbd9ee37a1ca7edad0eb"
key = bytes.fromhex("E0E0E0E0F1F1F1F1")

def decrypt(key, ciphertext):
    cipher = DES.new(key, DES.MODE_ECB)
    return unpad(cipher.decrypt(bytes.fromhex(ciphertext)), 8).decode()

print(decrypt(key, ciphertext))