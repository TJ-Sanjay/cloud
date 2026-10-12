import socket
import pickle
from data_object import DataObject

c=socket.socket()
c.connect(("localhost",12345))

obj=DataObject("sanjay",[1,2,3,4,5])
data=pickle.dumps(obj)

c.send(data)

res=c.recv(1024).decode()
print("res:",res)

c.close()
