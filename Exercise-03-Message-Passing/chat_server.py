import socket
import threading

HOST = "0.0.0.0"
PORT = 12347
clients = set()
clients_lock = threading.Lock()

def broadcast(message, sender):
    with clients_lock:
        targets = list(clients)
    for target in targets:
        try:
            target.sendall(message)
        except OSError:
            with clients_lock:
                clients.discard(target)
            try:
                target.close()
            except OSError:
                pass

def handle_client(conn, address):
    print(f"Connected: {address}")
    with conn:
        try:
            conn.sendall(b"Connected. Type /quit to leave.\n")
            stream = conn.makefile("rb")
            for raw in stream:
                message = raw.rstrip(b"\r\n")
                if message == b"/quit":
                    break
                if message:
                    line = f"{address}: ".encode() + message + b"\n"
                    print(line.decode(errors="replace").rstrip())
                    broadcast(line, conn)
        except OSError as exc:
            print(f"Client {address} error: {exc}")
        finally:
            with clients_lock:
                clients.discard(conn)
            print(f"Disconnected: {address}")

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen()
        print(f"Chat server listening on {HOST}:{PORT}")
        while True:
            conn, address = server.accept()
            with clients_lock:
                clients.add(conn)
            threading.Thread(target=handle_client, args=(conn, address), daemon=True).start()

if __name__ == "__main__":
    main()
