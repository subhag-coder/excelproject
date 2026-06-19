import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("DiwaliSales.csv")

#First view
"""print(df.head())
print(df.isnull().sum())"""

#Analysis
total_sales=df["Amount"]
total_orders=df["Orders"]
mostbuy_cate=df["Product_Category"].value_counts()
male_female=df["Gender"].value_counts()
states=df["State"].value_counts()
zone=df["Zone"].value_counts()
age_group=df["Age_Group"].value_counts()
occupation=df["Occupation"].value_counts()
unmarried=df[df["Marital_Status"]==0].shape[0]
married=df[df["Marital_Status"]==1].shape[0]
avg_order=df["Orders"].mean()
cust_moreavg=(df["Orders"]>avg_order).sum()

#Important Result

print("Total numbers of Orders:", total_orders.sum())
print("Total Sales:",total_sales.sum())
print("Average Number of orders per customer:",total_orders.mean())
print("Number of customers order more than average:",cust_moreavg)


#Who order more Male or Female
"""
plt.pie(male_female,labels=male_female.index, autopct='%1.2f%%')
plt.title("Orders placed by Male or Female")
plt.show()"""

#Top 5 states in term of highest orders
"""
top_5state=states.head(5)
top_5state.plot(kind='bar')
plt.title("Top Five States")
plt.ylabel("Number of orders")
plt.xlabel("States")
plt.grid()
plt.show()"""

#Top states in term of low orders placed
"""
low_states=states.tail(5)
low_states.plot(kind="bar", color="red", edgecolor='black')
plt.ylabel("Number of times orders placed")
plt.xlabel("States")
plt.title("Top States with Lowest Orders")
plt.show()
"""
#Top 5 product category
"""
tp_category=mostbuy_cate.head(5)
tp_category.plot(kind="bar", color="orange", edgecolor="black")
plt.title("Top Product Catgory")
plt.xlabel("Product Category")
plt.ylabel("Number of Times Customer Buy")
plt.show()"""

#Top Zones in Terms of Highest Orders
"""
zone.plot(kind="bar", color="pink", edgecolor="red")
plt.title("Top Zone With highest oders")
plt.xlabel("Zone")
plt.ylabel("Number of times order placed")
plt.grid()
plt.show()"""


#Age group with highest number of orders
"""
age_group.plot(kind="bar", color="green", edgecolor='red')
plt.title("Age Group wise Numbers of orders")
plt.ylabel("Numbers of Times orders")
plt.xlabel("Age Group")
plt.show()
"""
#Top custmer occupation who placed more orders.
"""
occupation.plot(kind='bar', color="brown", edgecolor="green")
plt.title("Custmer Occupation wise no. of Orders")
plt.xlabel("Occupation")
plt.ylabel("No. of times orders placed")
plt.grid()
plt.show()"""

#Who place orders more Married or Unmarried?
"""
size=[married,unmarried]
label=["Married","Unmarried"]
plt.pie(size,labels=label, explode=[0,0.1], autopct='%1.2f%%')
plt.title("Type of Customers who order more")
plt.show()"""

#Age-Group wise Percentage of orders (out of total orders)
"""
plt.pie(age_group,labels=(age_group.index+" Year"), autopct='%1.1f%%')
plt.title("Age-Group wise Percentage of Orders")
plt.show()"""
