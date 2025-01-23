# Question7: Multiplication Table Generator

def multiplication_table():
    
    number = int(input("Enter a number: "))

    print(f"Multiplication Table for {number}:")
    
    for i in range(1, 11):  #the loop multiplies 1 to 10 for the given number
        print(f"{number} x {i} = {number * i}")  #we are using string formatting in the print function for understandable output 


multiplication_table()
