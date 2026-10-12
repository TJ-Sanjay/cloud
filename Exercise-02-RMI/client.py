import Pyro4

def main():
    uri = input("Enter the server URI: ").strip()
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    with Pyro4.Proxy(uri) as calculator:
        print("Addition result:", calculator.add_numbers(a, b))
        print("Multiplication result:", calculator.multiply(a, b))

if __name__ == "__main__":
    main()
