#Question 10:  This program checks the number is armstrong 

def armstrong_num(num):#we are creating a function
    str_num=str(num)  #converting into string
    power=len(str_num) #length is noted
    return sum(int(digit)**power for digit in str_num)==num   #performing armstrong logic
num=int(input("Enter a number: "))
if armstrong_num(num):
    print("The given number is armstrong")
else:
    print("The given number is not armstrong")
