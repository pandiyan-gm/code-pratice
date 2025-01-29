#question 24. Write a Program to check the given number is divisible by both 3&4 if it is so print "Good Morning". If a number is divisible by only 4 but not 3 then print "Good Afternoon",
#If it is divisible by only 3 but not 4 then print "Good Evening" otherwise print "Good Night".?

def check_divisibility(num):
    if num%3 and num%4==0:    #we are using conditional operator and modulus to find the num is divisilibity 3,4
        print("Good Morning")
    elif num%4==0:
        print("Good Afternoon")
    elif num%3==0:
        print("Good Evening")
    else:
        print("Good Night")

num=int(input("Enter a number: "))
check_divisibility(num)
