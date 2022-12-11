import csv
data=[]
player_name=[]
Indcount=0
Engcount=0
Auscount=0

file=open("C:\\Users\\sornasree\\Desktop\\playerscore.csv","r")
file=csv.reader(file)
next(file) #remove the first row
print(file)

#store the csv file information in list
for value in file:
    data.append(value)
print(data)

#store the player name in a list
for value in range(0,len(data)):
    player_name.append(data[value][0])
print(player_name)

#calculate the number of players from each country
for value in range(0,len(player_name)):
    if "IND" in player_name[value] and set(player_name) :
        Indcount+=1
    
    if "ENG" in player_name[value] and set(player_name):
        Engcount+=1
    
    if "AUS" in player_name[value] and set(player_name):
        Auscount+=1
        
        
print("Indian player count is: ",Indcount)
print("England player count is: ",Auscount)
print("Australia player count is: ",Engcount)
