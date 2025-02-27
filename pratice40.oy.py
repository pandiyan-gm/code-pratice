#Given a number n, create and return a new int array of length n, containing the numbers 0, 1, 2, ... n-1. The given n may be 0, in which case just return a length 0 array. 
def create_arr(n):
    arr=[]
    for i in range(n):
        arr.append(i)   #adding elements to empty list 
    return arr

n=int(input("Enter a integer: "))
print(create_arr(n))


