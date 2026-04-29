def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Error: Division by zero")
    return a / b

def calculator():
    print("================================")
    print("       Simple Calculator        ")
    print("================================")
    print("Operations: +  -  *  /")
    print("Type 'exit' to quit")
    print("================================")

    while True:
        try:
            expr = input("\nEnter expression (e.g. 3 + 5): ").strip()
            if expr.lower() == 'exit':
                print("Goodbye!")
                break

            parts = expr.split()
            if len(parts) != 3:
                print("Invalid format. Use: <number> <operator> <number>")
                continue

            a, op, b = parts
            a, b = float(a), float(b)

            if op == '+':
                result = add(a, b)
            elif op == '-':
                result = subtract(a, b)
            elif op == '*':
                result = multiply(a, b)
            elif op == '/':
                result = divide(a, b)
            else:
                print(f"Unknown operator: {op}")
                continue

            print(f"Result: {a} {op} {b} = {result}")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == '__main__':
    calculator()
