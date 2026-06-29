

import sys

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b


def calculator():
    print("Available operations: +, -, *, /")
    print("Type 'quit' or 'exit' to end the program.\n")

    while True:
        
        operation = input("Enter operation (+, -, *, /) or 'quit' to exit: ").strip().lower()

        if operation in ('quit', 'exit'):
            print("Goodbye!")
            break

    
        if operation not in ('+', '-', '*', '/'):
            print("Invalid operation. Please enter one of +, -, *, /.\n")
            continue


        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number. Please enter numeric values.\n")
            continue


        try:
            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = subtract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            elif operation == '/':
                result = divide(num1, num2)

            print(f"{num1} {operation} {num2} = {result}\n")
        except ValueError as e:
            print(f"Error: {e}\n")
        except Exception as e:
            print(f"An unexpected error occurred: {e}\n")

if __name__ == "__main__":
    calculator()
