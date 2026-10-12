import Pyro4

uri=input("Enter the uri:")

calc=Pyro4.Proxy(uri)

a=int(input("a:"))
b=int(input("b:"))

print("add",calc.add(a,b))
print("multiply",calc.multiply(a,b))
