import argparse


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


# Maps the command line name to its function
OPERATIONS = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
}


def main():
    parser = argparse.ArgumentParser(prog="smart-calculator")
    parser.add_argument("operation", choices=OPERATIONS)
    parser.add_argument("a", type=float)
    parser.add_argument("b", type=float)
    args = parser.parse_args()

    print(OPERATIONS[args.operation](args.a, args.b))


if __name__ == "__main__":
    main()
