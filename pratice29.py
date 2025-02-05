#Question 34 This program prints the upper right and lower right triangle

n=5   
for i in range(n+1):
    for j in range(i):                      #we are using two loops for upper right triangle and two loops for lower right traingle
        print("*",end=" ")     
    print("* ")
for i in range(n):
    for j in range(i,n-1):
        print("*",end=" ")
    print("* ")
