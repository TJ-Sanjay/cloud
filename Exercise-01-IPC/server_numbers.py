import socket

HOST = "0.0.0.0"
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Number-sum server listening on {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        with conn:
            print("Connected:", addr)
            stream = conn.makefile("r", encoding="utf-8")
            for line in stream:
                message = line.strip()
                if message.lower() == "exit":
                    conn.sendall(b"Goodbye\n")
                    break
                try:
                    numbers = [int(part) for part in message.split()]
                    if not numbers:
                        raise ValueError("Enter at least one integer.")
                    result = sum(numbers)
                    conn.sendall(f"{result}\n".encode("utf-8"))
                except ValueError:
                    conn.sendall(b"ERROR: enter integers separated by spaces\n")
            stream.close()
