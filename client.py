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