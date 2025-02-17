#Question : This question generates a pin in which 3 inputs were given from that ones,tens,hundreds of pin should be least of three inputs and thousands of pin should max of all numbers in a input

def create_pin(input1,input2,input3):
    lis=[]
    x=str(input1)
    y=str(input2)
    z=str(input3)
        
    r=max(x[0],x[1],x[2],y[0],y[1],y[2],z[0],z[1],z[2])
    lis.append(r)
    k=min(x[0],y[0],z[0])
    lis.append(k)
    j=min(x[1],y[1],z[1])
    lis.append(j)
    p=min(x[2],y[2],z[2])
    lis.append(p)
    num = int("".join(map(str, lis)))    #we are appending the values in list and finally we are converting list into integer
    return num

input1=int(input("Enter a number :"))
input2=int(input("Enter a number :"))
input3=int(input("Enter a number :"))

print(create_pin(input1,input2,input3))

        
