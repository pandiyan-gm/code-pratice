#Question 20.You have a number to examine, and your mission is to write a program that checks 
#whether this number can be divided evenly by 27. Can you find out if it‟s a multiple of 27?

def num_examine(num):
    if num%27==0:
        print("The number is a multiple of 27")
    else:
        print("The number is not divisible of 27")

num=int(input("Enter a number: "))
num_examine(num)
