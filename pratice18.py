#question 18.Here we are giving some marks and name of the students as input from that we have to print second lowest score

nestlist=[]                                                                                                                     
tempscore=[]
result=[]                                                                                       
for _ in range(int(input())):
    name=input()
    score=float(input())
    nestlist.append([name,score])
    tempscore.append(score)

tempscore=sorted(list(set(tempscore)))         #we are adding the values in the list and sorting the score 
second_lowest_value=tempscore[1]

for i in range(len(nestlist)):
    if (nestlist[i][1]==second_lowest_value):      #iterating to the list and finding if any score matches
        result.append(nestlist[i][0])
    result.sort()
for i in result:
    print(i)

    #5
    #Harry
    #37.21
    #Berry
    #37.21
    #Tina
    #37.2
    #Akriti
    # 41
    # Harsh
    #39

#like this format we have to give input you can modify the input if required 
                                                                                                                                         


               
