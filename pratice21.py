#Question 26:You have two numbers, and your challenge is to write a program that performs both addition and subtraction with them. However,
#if any subtraction results in a negative number, display it as a positive value. How will you tackle this and show the final results?

def add_sub(num1,num2):
    add=num1+num2
    print(abs(add))
    sub=num1-num2
    print(abs(sub))

num1=int(input("Enter a number: "))
num2=int(input("Enter a number: "))
add_sub(num1,num2)
