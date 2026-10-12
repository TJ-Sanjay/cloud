import pickle
import socket
from data_object import DataObject

HOST = "0.0.0.0"
PORT = 12346

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Object server listening on {HOST}:{PORT}")
    conn, addr = server.accept()

    with conn:
        print("Connected:", addr)
        # Classroom demo: the object is small and the client is trusted.
        payload = conn.recv(65536)
        if not payload:
            raise RuntimeError("No object received.")
        obj = pickle.loads(payload)
        if not isinstance(obj, DataObject):
            raise TypeError("Expected a DataObject.")
        if not isinstance(obj.values, list) or not all(type(x) is int for x in obj.values):
            raise ValueError("values must be a list of integers.")
        print("Received object:", obj)
        conn.sendall(f"{sum(obj.values)}".encode("utf-8"))
