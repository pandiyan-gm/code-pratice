#Question no 11: Array Rotation based on the given Nth value

def rotate_arr(arr,n):
    n=n%len(arr)
    rotated_array=arr[n:]+arr[:n]       #performing rotation logic 
    return rotated_array

arr=list(map(int,input("enter the numbers: ").split( )))
n=int(input("enter the number of rotations: "))
result=rotate_arr(arr,n)

print(result)
