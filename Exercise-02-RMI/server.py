import os
import Pyro4

# Same-machine demo uses 127.0.0.1. For two VMs, start with
# PYRO_HOST=<server-private-IP> python server.py on the server VM.
SERVER_HOST = os.environ.get("PYRO_HOST", "127.0.0.1")
SERVER_PORT = 50000

@Pyro4.expose
class Calculator:
    def add_numbers(self, a, b):
        return int(a) + int(b)

    def multiply(self, a, b):
        return int(a) * int(b)

def main():
    daemon = Pyro4.Daemon(host=SERVER_HOST, port=SERVER_PORT)
    uri = daemon.register(Calculator())
    print("Calculator service is ready.")
    print("URI:", uri)
    daemon.requestLoop()

if __name__ == "__main__":
    main()
