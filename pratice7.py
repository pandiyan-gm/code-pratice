# Question7: Multiplication Table Generator
# This program generates a multiplication table for a number provided by the user.

def multiplication_table():
    # Taking input from the user
    number = int(input("Enter a number: "))

    print(f"Multiplication Table for {number}:")
    # Looping through 1 to 10 to generate the table
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

# Calling the multiplication table function
multiplication_table()
