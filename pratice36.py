#question return the minimum no of pages turning by comparing both front and back side 

def turn_count(n,p):
    return min(p//2,(n//2)-(p//2))  #we are using floor division which provides quotient 

n=int(input("Enter the total pages: "))
p=int(input("Enter the goal page: "))

print(turn_count(n,p))

