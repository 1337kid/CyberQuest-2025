import asyncio
import random
import string
import base64
from datetime import datetime
import pytz

def enc(key):
    plaintext = "cyberQuest{Bru73f0rc3_15_fun_d9778912f00b054e0c6cbb2768aea895}"
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
\033[96mWelcome to CatLand
Only a few elite minds can crack this encryption! (Base64-encoded)
Are you one of them?\033[0m

"""

PROMPT = """
\033[93mCan you guess the key? I'll tell you if it's correct.
Enter your guess: \033[0m"""

def get_ist_timestamp():
    ist = pytz.timezone('Asia/Kolkata')
    return datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S IST')

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"[{get_ist_timestamp()}] [+] Connection from {addr}")

    key = "".join(random.choices(string.ascii_letters + string.digits, k=12))
    encrypted_flag = enc(key)
    
    try:
        writer.write(BANNER.encode())
        writer.write(INFO.encode())
        writer.write(f"Encrypted flag: {encrypted_flag}\n".encode())
        writer.write(PROMPT.encode())
        await writer.drain()

        data = await reader.read(1024)
        received_key = data.decode(errors='ignore').strip()

        if received_key.startswith(("GET", "POST", "HEAD", "PUT", "DELETE", "OPTIONS", "CONNECT", "TRACE", "PATCH")):
            print(f"[{get_ist_timestamp()}] [!] Dropped HTTP request from {addr}")
            writer.close()
            await writer.wait_closed()
            return

        print(f"[{get_ist_timestamp()}] [{addr}] Received: '{received_key}'")

        if received_key == key:
            writer.write(b"\n\033[32mCorrect! Well done, agent.\033[0m\n")
        else:
            writer.write(b"\n\033[31mIncorrect! Access Denied.\033[0m\n")
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
