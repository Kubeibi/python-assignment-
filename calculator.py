def calculate(num1, num2, operation):
    """Performs a mathematical operation on two numbers."""
    if operation == "+":
        return f"{num1} + {num2} = {num1 + num2}"
    elif operation == "-":
        return f"{num1} - {num2} = {num1 - num2}"
    elif operation == "*":
        return f"{num1} * {num2} = {num1 * num2}"
    elif operation == "/":
        return f"{num1} / {num2} = {num1 / num2}" if num2 != 0 else "Error! Division by zero is not allowed."
    else:
        return "Invalid operation! Please enter one of +, -, *, /."


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")


print(calculate(num1, num2, operation))
