#question 17. In this program we are using ternary operator to check greatest amont three numbers

def ternary(a,b,c):
    return a if (a > b and a > c) else (b if b > c else c)    #It is ternary operator here we are checking the greatest number


a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
c=int(input("Enter a number: "))
print("The greatest number among three is: ",ternary(a,b,c))  
