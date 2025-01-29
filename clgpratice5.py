#question 25: This program finds the grade based on the given marks 

def find_grade(marks):
    if marks>=90: 
        print("Grade A")
    elif marks>=80 and marks<=89:               #conditional statements and comparison operators were used to evaluate the grade
        print("Grade B")
    elif marks>=70 and  marks<=79:
        print("Grade C")
    elif marks>=60 and marks<=69:
        print("Grade D")
    else:
        print("Grade F")
marks=int(input("Enter the marks: "))
find_grade(marks)
