import sys

def add(a, b):
    return(a + b)

def subtract(a, b):
    return(a - b)

def multiply(a, b):
    return(a * b)

def divide(a, b):
    return(a / b)

if __name__ == "__main__":
    choice = sys.argv[1]
    a = float(sys.argv[2])
    b = float(sys.argv[3])

    if choice == "add" or choice == "sum":
        print(f"{str(add(a, b)).removesuffix(".0")}")
    elif choice == "subtract":
        print(f"{str(subtract(a, b)).removesuffix(".0")}")
    elif choice == "multiply":
        print(f"{str(multiply(a, b)).removesuffix(".0")}")
    elif choice == "divide":
        print(f"{str(divide(a, b)).removesuffix(".0")}")
    else:
        print("Invalid choice entered")
