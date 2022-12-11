#The cafe owner has his cafe's sales data that includes total
# amount of sales in each day of the month.
#Find out the top 3 days when the sales was high and
# the 3 days when the sales was low.

import csv
data=[]
high_sale=[]
file = open("C:\\Users\\sornasree\\Desktop\\salesdetails.csv",'r') 
  
file = csv.reader(file) 
next(file) # it is use for remove first row which is header 
print(file)

#store the csv file in a data
for value in file:
   data.append(value)
print(data)

#conver the string in to integer
high_sale=[int(row[1]) for row in data if row]
print(high_sale)


high_sale.sort()
print(high_sale)

print("Top 3 the highest sales: ",high_sale[-1],",",high_sale[-2],",",high_sale[-3])
print("Top 3 lowest sales: ",high_sale[0],",",high_sale[1],",",high_sale[2])



