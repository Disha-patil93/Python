import pandas as pd

s1=pd.Series([1,2,3])
s2=pd.Series([20,45,67])
s3=pd.Series(['tara','sara','sanggu'])
d={"rollno":s1,"marks":s2,"names":s3,}
d2=pd.DataFrame(d)
#print(d)
print("after dataframes")
print(d2)
d3=d2.drop(2)
print(d3)

d4=d2.drop("marks",axis=1)
print(d4)
gk=d2.groupby("rollno").head()
print(gk)