import socket
import os
import time

SEPARATOR = ""
BUFFER_SIZE = 4096
host = "192.168.0.181"
port = 5003
filename = "test"

s = socket.socket()
print(f"[+] Connecting to {host}:{port}")
s.connect((host, port))
print("[+] Connected.")
try:
    while (True):    
        prevTime = time.time()
        with open(filename, "rb") as f:
            bytes_read = f.read(BUFFER_SIZE)
            if bytes_read:
                s.sendall(bytes_read)
        print(time.time() - prevTime)
        time.sleep(0.1)
except KeyboardInterrupt:
    print("End transfer")
    
s.close()
