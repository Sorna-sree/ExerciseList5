'''The cafe owner has his cafe's sales data that includes
total amount of sales in each day of the week.
Find out when the sales was high and when it was low.'''

import pandas as pd

data_file=pd.read_csv('sales.csv')


#FINDING MAX AND MIN
Max_value=data_file['total_amountof_sales'].max()
Min_value=data_file['total_amountof_sales'].min()


print("minimum value is: ",Min_value)
print("maximum value is",Max_value)

