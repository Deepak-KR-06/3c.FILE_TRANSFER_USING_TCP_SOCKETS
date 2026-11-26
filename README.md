# 3c.CREATION FOR FILE TRANSFER USING TCP SOCKETS
### Developed by: Deepak K R
### Reg No: 212225040057
## AIM
To write a python program for creating File Transfer using TCP Sockets Links
## ALGORITHM:
1. Import the necessary python modules.
2. Create a socket connection using socket module.
3. Send the message to write into the file to the client file.
4. Open the file and then send it to the client in byte format.
5. In the client side receive the file from server and then write the content into it.
## PROGRAM
### Server.py
```py
import socket

s = socket.socket()
s.connect(('localhost', 8000))

filename = input("Enter the filename: ")

s.send(filename.encode())

with open(filename, "rb") as f:
    while True:
        data = f.read(1024)
        if not data:
            break
        s.sendall(data)

s.shutdown(socket.SHUT_WR)

ack = s.recv(1024).decode()
print("Server:", ack)

s.close()
```
### Client.py
```py
import socket
from pythonping import ping

s = socket.socket()
s.bind(('localhost', 8000))
s.listen(5)

print("Server is waiting for connection...")

c, addr = s.accept()
print("Connected to:", addr)

while True:
    hostname = c.recv(1024).decode()

    if not hostname:
        break

    try:
        result = ping(hostname, verbose=False, count=1)
        c.send(str(result).encode())

    except Exception:
        c.send("Not Found".encode())

c.close()
s.close()
```
## OUPUT 
<img width="1917" height="1015" alt="image" src="https://github.com/user-attachments/assets/780dc0a5-39ea-4e96-a3ea-b9197ae4049c" />
<img width="823" height="280" alt="Screenshot 2026-11-26 142135" src="https://github.com/user-attachments/assets/9fc4d5f7-6be7-4552-ac7e-564daca9c392" />


## RESULT
Thus, the python program for creating File Transfer using TCP Sockets Links was 
successfully created and executed.
