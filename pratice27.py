#question 32.Given a non-empty array of integers nums, every element appears twice except for one. Find that single one. 

def single_number(num):
    for i in num:
        if num.count(i)==1:   #we printing the values in which count=1
            print(i,end=" ")


num=list(map(int,input("Enter the numbers: ").split()))
(single_number(num))


