#question 21.This program checks whether the given character is vowel or consonant 

def findtype(s):
    vowels='aeiou'
    if s in vowels:               #we are checking through the condition
        return True
    else:
        return False

s=input("enter a char: ")
if findtype(s):
    print("The given character is a vowel")
else:
    print("The given character is a consonant")

