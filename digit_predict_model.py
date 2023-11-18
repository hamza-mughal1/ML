import pickle
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import datasets
import pandas as pd 

# Load the digits dataset
digits = datasets.load_digits()
# plt.gray()
# print(set(digits["data"][7]))
# plt.matshow(digits["images"][7])
# plt.show()

x = digits["data"]
y = digits["target"]


data = {}
for t in range(64):
    data[t] = []

for i in list(x):
    for j in range(64):
        data[j].append(i[j])

data["target"] = list(y)

df = pd.DataFrame(data)
df.to_csv("digit_data.csv",index=False)

# x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.3)

# model = LogisticRegression(max_iter=10000)
# model.fit(x,y)

# print("Done!")

# print(model.score(x_test,y_test))

# with open ("digit_model","wb") as f:
#     pickle.dump(model,f)



# with open ("digit_model","rb") as f:
#     model = pickle.load(f)



