import socket
import threading

HOST = "127.0.0.1"
PORT = 12347

def receive_messages(sock):
    stream = sock.makefile("r", encoding="utf-8")
    try:
        for line in stream:
            print(line.rstrip())
    except OSError:
        pass

def main():
    with socket.create_connection((HOST, PORT)) as client:
        threading.Thread(target=receive_messages, args=(client,), daemon=True).start()
        try:
            while True:
                message = input()
                client.sendall((message + "\n").encode("utf-8"))
                if message.strip() == "/quit":
                    break
        except (EOFError, KeyboardInterrupt):
            try:
                client.sendall(b"/quit\n")
            except OSError:
                pass

if __name__ == "__main__":
    main()
