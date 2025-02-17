#question: this program prints the pattern of curly braces "{}"

n=int(input("Enter a number: "))
for i in range(1,n+1):    
    for j in range(i+1):      #here it prints next to next 
        for k in range(j):
            print("{",end="")     #we are using j to print open braces  in same line 
        for l in range(j):
            print("}",end="")   #in same way close braces are done
        print(end=" ")    #this is for space between a single set
    print('')   
        
        
