#Question 19. This question prints the substring of the given string


def sub_str(str1):
    for i in range(len(str1)):         #this loop takes the length of the string 
        for j in range(i + 1, len(str1) + 1):   #and increments the value and removes after use
            print(str1[i:j])

str1=input("Enter a string: " )
sub_str(str1)
