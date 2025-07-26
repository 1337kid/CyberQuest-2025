from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad
import binascii

hex_ciphertext = "b25431b1548dc978182bfd9249d5c6fb2e2d1b740b1a30901fe78a9b0527449c380ad4fd9ce798a0d0a57fe924827325b45c9d0905ddcf69b7074babf61ffbd9ee37a1ca7edad0eb"
ciphertext = bytes.fromhex(hex_ciphertext)

weak_keys = [
    bytes.fromhex("0101010101010101"),
    bytes.fromhex("FEFEFEFEFEFEFEFE"),
    bytes.fromhex("E0E0E0E0F1F1F1F1"),
    bytes.fromhex("1F1F1F1F0E0E0E0E")
]

for i, key in enumerate(weak_keys):
    try:
        cipher = DES.new(key, DES.MODE_ECB)
        decrypted = unpad(cipher.decrypt(ciphertext), 8)
        print(f"Key #{i+1}: {key.hex()} => Decrypted text: {decrypted.decode()}")
    except Exception as e:
        print(f"Key #{i+1}: {key.hex()} => Failed to decrypt: {e}")
