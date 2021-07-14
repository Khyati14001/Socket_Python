import socket

s = socket.socket()
print('Socket Created')
s.bind(("localhost",9999))

s.listen(3) #buffered for 3 connections means 3 client can connect

print("Wating for connections")

while True:
    c , addr = s.accept()
    name= c.recv(1024).decode()
    print("Connected with",addr,name)
    c.send(bytes("Welcome","utf-8"))

    c.close()