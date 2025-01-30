#question 30. this program checks if the sentence is a palindrome or not 

def palindrome_checker(string):
    cleaned_string=''.join(char for char in string if char.isalnum())  #we are removing non alpha numeric characters 
    clean_str=cleaned_string.lower()  #strings converted into lowercase
    return clean_str==clean_str[::-1]  

string=input()
if palindrome_checker(string):
    print("True")
else:
    print("False")
