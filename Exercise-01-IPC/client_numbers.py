import socket

HOST = "127.0.0.1"  # Replace with server VM private IP for a multi-VM test.
PORT = 12345

with socket.create_connection((HOST, PORT)) as client:
    stream = client.makefile("r", encoding="utf-8")
    while True:
        message = input("Enter integers separated by spaces (or exit): ").strip()
        client.sendall((message + "\n").encode("utf-8"))
        response = stream.readline()
        if not response:
            print("Server disconnected.")
            break
        print("Server response:", response.strip())
        if message.lower() == "exit":
            break
    stream.close()
