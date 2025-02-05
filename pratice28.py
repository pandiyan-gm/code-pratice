#question 33 This program calculates the GCD of two numbers 

def gcd(a,b):
    if a>b:
        a,b=b,a     #swapping the value if a greater than b
    while b:
        a,b=b,b%a    #using modulus operator to find GCD
    return a

a=int(input("Enter a number : "))
b=int(input("Enter a number : "))
print(gcd(a,b))
