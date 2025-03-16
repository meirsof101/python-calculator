# Simple Calculator Program
# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Perform the operation
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:
        print("Error! Division by zero is not allowed.")
        exit()  # Stop execution if division by zero
    result = num1 / num2
else:
    print("Invalid operation! Please enter +, -, *, or /.")
    exit()  # Stop execution if the input is invalid

# Print the result with formatting
print(f"{num1} {operation} {num2} = {int(result) if result.is_integer() else result}")
