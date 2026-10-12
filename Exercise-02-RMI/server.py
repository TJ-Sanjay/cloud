import Pyro4

@Pyro4.expose
class clac:
    def add(self,a,b):
        return a+b
    def multiply(self,a,b):
        return a*b

daemon=Pyro4.Daemon()
uri=daemon.register(clac)

print("server is ready")
print("Uri",uri)

daemon.requestLoop()
