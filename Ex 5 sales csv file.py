import csv
data=[] #store the csv file datas
week1=0
week2=0
week3=0
week4=0
total_sales=[]
highest_week=0
lowest_week=0

file = open("C:\\Users\\sornasree\\Desktop\\salesdetails.csv",'r')

file = csv.reader(file)
next(file) # it is use for remove first row which is header

#store the csv file in data
for value in file:
    data.append(value)
start_date=0
end_date=7
def week_calculation(start_date,end_date):
    for index in range(start_date,end_date):
        week1+=int(data[index][1])
    total_sales.append(week1)
    


#calculate the totalsales of week1
for index in range(0,7):
    week1+=int(data[index][1])
total_sales.append(week1)

#calculate the totalsales of week2
for index in range(7,14):
    week2+=int(data[index][1])
total_sales.append(week2)

#calculate the totalsales of week3
for index in range(14,21):
    week3+=int(data[index][1])
total_sales.append(week3)

#calculate the totalsales of week4
for index in range(21,len(data)):
    week4+=int(data[index][1])
total_sales.append(week4)

print(total_sales)

#find the minimum and maximum value
maximum=(max(total_sales))
minimum=(min(total_sales))


#find the maximum and minimum value index
for index in range(0,len(total_sales)):
    if(total_sales[index] == maximum):
        highest_week = index
    if(total_sales[index] == minimum):
        lowest_week = index
print(highest_week)
print(lowest_week)

#create the output file
with open('output_cafe.csv','w') as ans:
    data = csv.writer(ans)
    data.writerow(("high sale week","low sale week"))
    data.writerow((highest_week + 1,lowest_week+ 1))

print(open('output_cafe.csv').read())