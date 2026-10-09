import math

history = []

def calculate(a, op, b=None):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/':
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    if op == '**': return a ** b
    if op == 'sqrt': return math.sqrt(a)
    raise ValueError(f"Unknown operator: {op}")

def main():
    print("=== Python Calculator ===")
    print("Operators: +  -  *  /  **  sqrt")
    print("Type 'history' to see past calculations, 'quit' to exit\n")

    while True:
        user_input = input("Enter expression (e.g. 5 + 3): ").strip()
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        if user_input.lower() == 'history':
            if not history:
                print("No history yet.")
            else:
                for i, h in enumerate(history, 1):
                    print(f"  {i}. {h}")
            continue
        parts = user_input.split()
        try:
            if len(parts) == 2 and parts[0] == 'sqrt':
                a = float(parts[1])
                result = calculate(a, 'sqrt')
                expr = f"sqrt({a}) = {result}"
            elif len(parts) == 3:
                a, op, b = float(parts[0]), parts[1], float(parts[2])
                result = calculate(a, op, b)
                expr = f"{a} {op} {b} = {result}"
            else:
                print("Invalid input. Try: 5 + 3 or sqrt 16")
                continue
            print(f"Result: {result}")
            history.append(expr)
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
