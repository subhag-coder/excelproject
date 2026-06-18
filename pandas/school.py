import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("School.csv")
inactive=df[df["SchoolStatus"]=="InActive"].shape[0]
active=df[df["SchoolStatus"]=="Active"].shape[0]
private=df[df["SchoolType"]=="PRI"].shape[0]
public=df[df["SchoolType"]=="PUB"].shape[0]
state=df["SchoolState"].value_counts()
city=df["SchoolCity"].value_counts()
city5=city.head(5)
semtype=df[df["TermType"]=="SEM"].shape[0]
qtrtype=df[df["TermType"]=="QTR"].shape[0]


print("No. of Unactive school:",inactive)
print("No. of active school:",active)
print("Total no. of private school:",private)
print("Total no. of public school:",public)
print("State with highest no. of school:",state.head(1))
print("No. of school with sem term type: ",semtype)
print("No. of school with quaterly term type:",qtrtype)
print("City with highest no. of school:",city.head(1))
"""
state.plot(kind="bar")
plt.title("State wise number of schools")
plt.ylabel("Number of School")
plt.grid(True)
plt.show()
"""
"""city5.plot(kind="bar", color=['blue', 'black','orange','green','red'])
plt.title("Top five city")
plt.ylabel("Numbers of School")
plt.grid()
plt.show()"""

"""
size=[active,inactive]
plt.pie(size, labels=["Active","Inactive"], autopct="%1.2f", explode=[0,0.2])
plt.title("Percentage of Active vs Inactive Schools")
plt.show()"""

"""
ppsize=[public,private]
plt.pie(ppsize, labels=["Public", "Private"], autopct='%1.2f%%')
plt.title("Public Vs Private Schools")
plt.show()"""
"""
termsize=[semtype,qtrtype]
labels=["Semester", "Quaterly"]
bars=plt.bar(labels,termsize, color=["orange", "red"])
plt.bar_label(bars)
plt.title("School Term Type")
plt.xlabel("Term Type")
plt.ylabel("Number of Schools")
plt.show()

"""