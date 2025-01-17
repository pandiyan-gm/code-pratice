#Question 9. This question prints the unique and duplicate values separately present in the list

arr1=[2,4,6,2,6,3,5,4,7,8,9]  #this is the list contains values
unique_values=set()    #creating empty sets
duplicate_values=set()
for i in arr1:  #looping through the list
    if i in unique_values:  
        duplicate_values.add(i)  #adding values in the set
    else:
        unique_values.add(i)
unique_values=unique_values-duplicate_values  #using difference operator to remove duplicate values
print("Unique values are: ",unique_values)
print("Duplicate values are: ",duplicate_values) 
