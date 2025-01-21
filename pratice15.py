#Question 15:This swap the uppercase letters to lowercase and viceversa

def swap_case(word):
    swapped=""
    for char in word:
        if char.isupper():   #It checks if the char is uppercase and swap them into lower if not switch into other condition
            swapped+=char.lower()   
        elif char.islower():
            swapped+=char.upper()
        else:
            swapped+=char
    return swapped
word=input("Enter a word: ")
print("The word after swapping is",swap_case(word))
