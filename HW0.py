
import os
os.getcwd()
os.chdir('C:\\Users\\Adil Ashish Kumar\\Desktop')
import pandas as pd
# 1. Read the data and store it
df = pd.read_csv("foodorders.tsv",sep='\t')
# 2. Print the first 5 observations of the data set
df[:5]
# 3. Print the number of rows AND the number of columns in the data set
print("the no of rows in the data is " + str(df.shape[0]))
print("the no of columns in the data is " + str(df.shape[1]))
# 4. What is the most ordered item in the dataset and how many times was this item ordered?
a=df.groupby('item_name').count().order_id.sort_values(ascending=False).reset_index()
print("the most ordered item is " + str(a.iloc[0,0]) + " ,and it was ordered " + str(a.iloc[0,1])+" times")
#5. What is the total revenue the firm earned?
df['quantity'] = df['quantity'].astype(float)
df['price'] =df['item_price'].str[1:]
df['price'] = df['price'].astype(float)
df['revenue'] = df['quantity'] * df['price']
print("the total revenue the firm earned is $" + str(df['revenue'].sum()))
# 6. What is the average amount per order?
print("the avg revenue per order is $" + str(round(df['revenue'].sum()/df['order_id'].nunique(),2)))
# 7. How many distinct items were ordered in the data set?
print(str(df['item_name'].nunique()) + " distinct items were ordered in the data set")