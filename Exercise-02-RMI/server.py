import os
import Pyro4

SERVER_HOST = os.environ.get("PYRO_HOST", "0.0.0.0")
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
    print("For a remote client, use a URI with the server's reachable IP.")
    daemon.requestLoop()

if __name__ == "__main__":
    main()
