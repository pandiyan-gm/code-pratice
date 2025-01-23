#question 8: Age group classifcation

def age_grp(age):
    if age<0:       #using Conditions to validate the age
        print("Invalid age")
    elif age<=12:
        print("Child")
    elif age<=19:
        print("Teenager")
    elif age<=64:
        print("Adult")
    else:
        print("senior")
age=int(input("Enter the age: "))
age_grp(age)
    
