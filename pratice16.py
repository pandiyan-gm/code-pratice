#This program will use all comparison operators to validate the number
def compare_numbers(num1, num2):

    if num1 > num2:                                              #here we are using if and else condition to validate all the comparison operators
        print(num1, ">", num2, ": True")
    else:
        print(num1, ">", num2, ": False")

    if num1 >= num2:
        print(num1, ">=", num2, ": True")
    else:
        print(num1, ">=", num2, ": False")

    if num1 < num2:
        print(num1, "<", num2, ": True")
    else:
        print(num1, "<", num2, ": False")

    if num1 <= num2:
        print(num1, "<=", num2, ": True")
    else:
        print(num1, "<=", num2, ": False")

    if num1 == num2:
        print(num1, "==", num2, ": True")
    else:
        print(num1, "==", num2, ": False")

    if num1 != num2:
        print(num1, "!=", num2, ": True")
    else:
        print(num1, "!=", num2, ": False")


num1=int(input("enter a number: ")) 
num2 =int(input("enter a number: "))
compare_numbers(num1, num2)
