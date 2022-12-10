#Print all the players with Highest score and not out.
import csv
data=[]



file=open("C:\\Users\\sornasree\\Desktop\\playerscore.csv","r")
file=csv.reader(file)
next(file)   

for value in file:
    data.append(value)
#print(data)
high_scorelist=[]

#store the highest score in a list
for value in range(0,len(data)):
    high_scorelist.append(data[value][6])
print(high_scorelist)

#find the not out in the highestscore list
for value in range(0,len(high_scorelist)):
    if  "*" in high_scorelist[value]:
        print(data[value][0],"highest score is",high_scorelist[value])
        
