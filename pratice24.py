#question 29. this program prints the range of n we are given which prints some word based on the condition in a list

n=int(input())
output=[]
for i in range(1,n+1):   #This loop ranges starting from 1 to nth number 
    if i%3==0 and i%5==0:       #we are using conditional operator and modulus to find the result
        output.append("FIZZBUZZ") 
    elif i%3==0:
        output.append("FIZZ")
    elif i%5==0:
        output.append("BUZZ")
    else:
        output.append(str(i))

print(output)     #appending the results into the list and printing 
