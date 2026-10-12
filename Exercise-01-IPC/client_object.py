import pickle
import socket
from data_object import DataObject

HOST = "127.0.0.1"  # Replace with server VM private IP for a multi-VM test.
PORT = 12346

name = input("Enter name: ").strip()
values_text = input("Enter integer values separated by spaces: ").strip()
values = [int(item) for item in values_text.split()]
obj = DataObject(name, values)

with socket.create_connection((HOST, PORT)) as client:
    client.sendall(pickle.dumps(obj))
    print("Sum returned by server:", client.recv(1024).decode("utf-8"))
