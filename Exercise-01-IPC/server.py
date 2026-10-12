import socket

s=socket.socket()
s.bind(("localhost",12345))
s.listen()

print("server waiting")
c,addr=s.accept()
print("client connected")

while True:
    data=c.recv(1024).decode()

    if data=="exit" or not data:
        break
    nums=list(map(int,data.split()))
    tot=sum(nums)

    c.send(str(tot).encode())
    print("tot",tot)

c.close()
s.close()
