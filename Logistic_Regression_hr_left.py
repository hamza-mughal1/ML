import pandas as pd
import pickle
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("HR_comma_sep.csv")
x = (df)

# plt.scatter(df["salary"],df["left"])
# plt.show()

x = []
y = df["left"]
x1 = df["salary"]
x2 = df["satisfaction_level"]
for i in range(len(df["salary"])):
    x.append([x1[i],x2[i]])

x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.3)

y_test_list = list(y_test)

model = LogisticRegression()
model.fit(x_train,y_train)

predicted = model.predict(x_test)
for i in range(50):
    print(f"predicted = {predicted[i]}, original = {y_test_list[i]}")

print(model.score(x_test,y_test))

with open ("Hr_left_model","wb") as f:
    pickle.dump(model,f)

