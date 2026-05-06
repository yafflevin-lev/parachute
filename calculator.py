def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def calculate(a, operator, b):
    ops = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }
    if operator not in ops:
        raise ValueError(f"Unknown operator: {operator}")
    return ops[operator](a, b)


def main():
    print("Basic Calculator")
    print("Operators: +  -  *  /")
    print("Type 'quit' to exit\n")

    while True:
        expression = input("Enter expression (e.g. 3 + 5): ").strip()
        if expression.lower() == "quit":
            break
        parts = expression.split()
        if len(parts) != 3:
            print("Error: enter in format: <number> <operator> <number>")
            continue
        try:
            a, operator, b = float(parts[0]), parts[1], float(parts[2])
            result = calculate(a, operator, b)
            print(f"= {result}\n")
        except ValueError as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    main()
