#question 31. A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself.
#A divisor of an integer x is an integer that can divide x evenly. Given an integer n, return true if n is a perfect number, otherwise return false. 

def perfect_number(a):
    c=0
    for i in range(1,a):   #here we are checking the number which divides a and produce remainder as 0
        if a%i==0:      
            c+=i
    print(a==c)

a=int(input("Enter a number: "))
perfect_number(a)
