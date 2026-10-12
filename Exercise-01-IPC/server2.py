import socket
import pickle

s=socket.socket()
s.bind(("localhost",12345))
s.listen()

print("server waiting")
c,addr=s.accept()
print("client connected")

data=c.recv(4096)
obj=pickle.loads(data)

print("name",obj.name)
print("value",obj.value)

tot=sum(obj.value)
c.send(str(tot).encode())

c.close()
s.close()
