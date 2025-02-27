#Question this prints the value in the given array which occurs more than once

def repeat(arr):
    word={}
    lis=[]
    for i in arr:
        if i in word:    #we are appending them in dictionary to get count 
            word[i]+=1
        else:
            word[i]=1
    for i,key in word.items():
        if key>1:   #appending the value in a list which has key value greater than 1
            lis.append(i)
    return lis

arr=[2, 3, 1, 2, 3]
print(repeat(arr))
            
