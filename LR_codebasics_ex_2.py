import pandas 
from sklearn import linear_model
from word2number import w2n

df = pandas.read_csv("hiring.csv")


df["experience"] = df["experience"].fillna("zero")

f = []
for i in df["experience"]:
    f.append(w2n.word_to_num(i))

df["experience"] = f


def foo(dataset):
    l = []
    for i in range(len(dataset["experience"])):
        l.append([int(dataset["experience"][i]),int(dataset["test_score(out of 10)"][i]),int(dataset["interview_score(out of 10)"][i])])
    return l

df["test_score(out of 10)"] = df["test_score(out of 10)"].fillna(df["test_score(out of 10)"].median())

data_x = foo(df.drop(columns=["salary($)"]))
data_y = []
for i in df["salary($)"]:
    data_y.append(i)


model = linear_model.LinearRegression()
model.fit(data_x,data_y)

pred = model.predict([[12,10,10]])
print(pred)