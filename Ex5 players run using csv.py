import csv
data=[]
runs_list=[]


file=open("C:\\Users\\sornasree\\Desktop\\index.csv","r")
file=csv.reader(file)
next(file) #remove the first row

#store the csv file information in list
for value in file:
    data.append(value)
print(data)

#store the runs in list
for runs in range(0,len(data)):
    runs_list.append(data[runs][5])
print(runs_list)


#sorting the list
runs_list.sort()
#runs_list.sort(key=int)

print(runs_list)


print("first winner: ",runs_list[-1])
print("second winner: ",runs_list[-2])


