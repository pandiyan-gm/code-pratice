#question 22.This program checks the biggest among two numbers 

def findbig(num1,num2):
    if num1>num2:                           #we are using comparison operator is to validate  
        print("num 1 is greater")
    else:
        print("num 2 is greater")

num1=int(input("enter a num: "))
num2=int(input("Enter a num:  "))
findbig(num1,num2)

             
