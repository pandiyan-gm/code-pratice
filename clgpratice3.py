#question 23. find the number belonging to which group above 50,between 40-50,less than 40?

def findgroup(num1):
    if num1<40:
        print("The num is 1st grp")
    elif num1>=40 and num1<=50:                   #here we are using conditional operator to find the number group 
        print("The num is 2nd grp")
    else:
        print("The num is third grp")
num1=int(input("Enter a number: "))
findgroup(num1)
