#Question this checks the given array has 7 continously or separated by one num if it has it returns true or it will return false
def has77(arr):
    for i in range(len(arr)-1):
        if arr[i]==7 and arr[i+1]==7:   #ensuring 7 using conditional statements and indexing
            return True
        elif arr[i]==7 and arr[i+2]==7:
            return True
        else:
            return False
arr=[7, 2,7, 3, 7]
print(has77(arr))

    
