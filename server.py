import socket

s = socket.socket()
s.bind(('localhost', 8000))
s.listen(1)

print("Server is waiting for connection...")

c, addr = s.accept()
print("Connected to:", addr)

filename = c.recv(1024).decode()

with open("received_" + filename, "wb") as f:
    while True:
        data = c.recv(1024)
        if not data:
            break
        f.write(data)

print("File received successfully")

c.send("File received successfully".encode())

c.close()
s.close()