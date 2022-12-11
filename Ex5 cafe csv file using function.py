import csv 
data=[] #store the csv file datas 
week1=0 
week2=0 
week3=0 
week4=0 
total_sales=[] 
highest_week=0 
lowest_week=0 
start_date=0
end_date=7

  
file = open("C:\\Users\\sornasree\\Desktop\\salesdetails.csv",'r') 
  
file = csv.reader(file) 
next(file) # it is use for remove first row which is header 
  
 #store the csv file in data 
for value in file: 
     data.append(value) 

#calculate the total sales of per week
def week_calculation(start_date,end_date,week): 
     for index in range(start_date,end_date): 
         week+=int(data[index][1]) 
     return week
     
week1=week_calculation(0,7,week1)
total_sales.append(week1)

week2=week_calculation(7,14,week2)
total_sales.append(week2)

week3=week_calculation(14,21,week1)
total_sales.append(week3)

week4=week_calculation(21,len(data),week2)
total_sales.append(week3)

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
print("Highest week index:",highest_week) 
print("Lowest week index: ",lowest_week) 

 #create the output file 

with open('output_cafe.csv','w') as ans: 
     data = csv.writer(ans) 
     data.writerow(("high sale week","low sale week")) 
     data.writerow((highest_week + 1,lowest_week+ 1)) 
  
open('output_cafe.csv').read()

print("Highest week: ",highest_week+1)
print("lowest week; ",lowest_week+1)
