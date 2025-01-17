def are_anagrams(str1,str2):
    str1=str1.replace(" ","").lower()
    str2=str2.replace(" ","").lower()
    return sorted(str1)==sorted(str2)

word1=input("enter a word: ")
word2=input("enter a word: ")

if are_anagrams(word1,word2):
    print("the given words are anagrams")
else:
    print("the given words are  not anagrams")
