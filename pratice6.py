# question6: Simple Calculator
# This program performs basic arithmetic operations: addition, subtraction, multiplication, and division.

def calculator():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    # Taking input from the user
    choice = input("Enter choice (1/2/3/4): ")

    # Taking two numbers as input
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Performing the selected operation
    if choice == '1':
        print(f"The result is: {num1 + num2}")
    elif choice == '2':
        print(f"The result is: {num1 - num2}")
    elif choice == '3':
        print(f"The result is: {num1 * num2}")
    elif choice == '4':
        if num2 != 0:
            print(f"The result is: {num1 / num2}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid input")

# Calling the calculator function
calculator()
