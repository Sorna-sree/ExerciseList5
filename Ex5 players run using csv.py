import csv
data=[]
runs_list=[]


file=open("C:\\Users\\sornasree\\Desktop\\playerscore.csv","r")
file=csv.reader(file)
next(file) #remove the first row
print(file)

#store the csv file information in list
for value in file:
    data.append(value)
print(data)

for value in range(0,len(data)):
    runs_list.append(data[value][5])

#string is converted to the integer
runs_list=[int(i) for i in runs_list]
print(runs_list)

#print(len(runs_list))

#print the differents of the two players
for index in range(0,len(runs_list),1):
    player1=(runs_list[index])-(runs_list[index+1])
    player2=(runs_list[index+1])-(runs_list[index+2])
    print("player1: ",player1)
    print("player2: ",player2)


