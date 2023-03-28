import socket
import tqdm
import os
import time
import re
# device's IP address
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5001
# receive 4096 bytes each time
BUFFER_SIZE = 1024
filename = "D:/test"

s = socket.socket()
s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
client_socket, address = s.accept()
print(f"[+] {address} is connected.")
pattern = re.compile(r'\([^)]*\)$')

try:
    while True:
        # read 1024 bytes from the socket (receive)
        bytes_read = client_socket.recv(BUFFER_SIZE).decode()
        if bytes_read:
            match = pattern.search(bytes_read)
            if match:
                print(match.group(0)[2:-2])
                try:
                    with open(filename, "w") as f:
                        f.write(match.group(0)[2:-2])
                except PermissionError:
                    pass
            else:
                print("No match")
                pass
        time.sleep(0.02)
except KeyboardInterrupt:
    print("Ending connection")
    client_socket.close()
    s.close()

# # close the client socket
# client_socket.close()
# # close the server socket
# s.close()