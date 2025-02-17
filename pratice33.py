#Question: this prints the array elements with required number we want and append it in new array
x=int(input("Enter a number: "))   
a=[1,2,3,4,5,6,7,8,9,10]
b=[]
for i in a:
    b.append(x*i)     #here we are append the new elements by multiplying with the number we want   
print(b)
