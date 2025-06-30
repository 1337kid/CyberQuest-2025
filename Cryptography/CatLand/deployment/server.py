import asyncio
import random
import string
import base64
from datetime import datetime
import pytz
from wonderwords import RandomSentence

flag = "cyberQuest{Bru73f0rc3_15_fun_d9778912f00b054se0c6cbb2768aea895}"

def enc(plaintext, key):
    enc = ""
    for i in range(len(plaintext)):
        enc += chr(ord(plaintext[i]) ^ ord(key[i % len(key)]))
    return base64.b64encode(enc.encode()).decode()

BANNER = """
\033[34m                          /\\       
                         /  \\    /\\         /\\       
   /\\      /\\           /    \\  /  \\  /\\   /  \\    
  /  \\    /  \\    /\\   /      \\/    \\/  \\ /    \\   
 /    \\  /    \\  /  \\_/     2025      /\\_/      \\   
\033[37m--------------------------------------------------
\033[32m       .    EXCEL .     .  .  .         .      
 .     .        .     .    .      .       .    .    
       /\\     /\\     .      .      .     .         
    . {  `---'  }      . Welcome to...                
      {  O   O  }     .          \033[36mCatLand\033[32m        
 .    ~~>  V  <~~     .        .     Meow~         .       
       \\  \\|/  /                                
  .   . `-----'     .      .      .     .          
    .  \033[90mMeow say xorry\033[0m
"""

INFO = """
\033[96m[!] You have approached the gates of CatLand.
\033[96m[!] Here is your encrypted one time password! (Base64-encoded)
\033[0m
"""

PROMPT = """
\033[93m[!] Submit the one time password to prove you are a CatLandian: \033[0m"""

def get_ist_timestamp():
    ist = pytz.timezone('Asia/Kolkata')
    return datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S IST')

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"[{get_ist_timestamp()}] [+] Connection from {addr}")

    key = "".join(random.choices(string.ascii_letters + string.digits, k=9))
    plaintext = f'catland-{RandomSentence().sentence().replace(" ", "-").replace(".","")}'
    encrypted_password = enc(plaintext, key)
    
    try:
        writer.write(BANNER.encode())
        writer.write(INFO.encode())
        writer.write(f"[+] Encrypted password: {encrypted_password}\n".encode())
        writer.write(PROMPT.encode())
        await writer.drain()

        data = await reader.read(1024)
        received_password = data.decode(errors='ignore').strip()

        if received_password.startswith(("GET", "POST", "HEAD", "PUT", "DELETE", "OPTIONS", "CONNECT", "TRACE", "PATCH")):
            print(f"[{get_ist_timestamp()}] [!] Dropped HTTP request from {addr}")
            writer.close()
            await writer.wait_closed()
            return

        print(f"[{get_ist_timestamp()}] [{addr}] Received: '{received_password}'")

        if received_password == plaintext:
            writer.write(b"\n\033[32m[+] Correct! You are a CatLandian.\033[0m\n")
            writer.write(f"[!] Here is the flag: {flag}\n".encode())
        else:
            writer.write(b"\n\033[31m[-] Incorrect! Access Denied.\033[0m\n")
        await writer.drain()

    except Exception as e:
        print(f"[{get_ist_timestamp()}] [-] Error with {addr}")
    finally:
        writer.close()
        await writer.wait_closed()
        print(f"[{get_ist_timestamp()}] [-] Connection with {addr} closed")

async def main():
    server = await asyncio.start_server(handle_client, '0.0.0.0', 12345)
    print(f"[{get_ist_timestamp()}] [*] Async server running on port 12345")
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
