import pandas as pd 
from sklearn import linear_model

df = pd.read_csv("homeprices.csv")

x = df["area"]
y = df["price"]

f_x = [[i] for i in x]
f_y = [i for i in y]


reg = linear_model.LinearRegression()
reg.fit(f_x,f_y)
r = reg.predict([[2020]])
new_row = [2020,r[0]]

df = df._append(new_row, ignore_index=True)

df.to_csv("homeprices.csv",index=False)

