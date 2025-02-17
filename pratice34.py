#Question: this takes the number and replace it with 0 and append at last of the list 
def replace(arr,n):
    i = 0
    while i < len(arr):
        if arr[i]== n:
            arr.pop(i)
            arr.append(0)
            i-=1     #this is for not skipping the next digit 
        i+=1
    return arr

n = int(input("Enter the number to replace : "))
arr = [1,2,4,6,6,23,68,345]
print(replace(arr,n))
