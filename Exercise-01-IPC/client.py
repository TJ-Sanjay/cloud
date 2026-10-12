import socket

c=socket.socket()
c.connect(("localhost",12345))

while True:

    msg=str(input("enter numver or exit:"))

    if msg=="exit":
        c.send(msg.encode())
        break
    c.send(msg.encode())
    res=c.recv(1024).decode()
    print("sum",res)
c.close()
