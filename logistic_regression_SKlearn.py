from sklearn.linear_model import LogisticRegression
from sklearn.metrics import log_loss
import numpy as np

# hour / 8, practice / 5, test / 15, attendance / 260, practical / 10

data_x_train = np.array([[3],[4.5],[2],[6],[2],[3.5]])
# data_x_test = np.array([[3,1,5,140,4],[5,3.6,13,186,7],[1,0.3,4,150,5],[6.3,3.2,12,220,9],[3,2,9,190,6],[3,2.1,8,183,5]])

data_y_train = np.array([0,1,0,1,1,1])
# data_y_test = np.array([0,1,0,1,1,0])

model = LogisticRegression()

model.fit(data_x_train,data_y_train)

# y_predict = model.predict(np.array(data_x_test))

# print(y_predict)
# print(log_loss(data_y_test,y_predict))
print(model.coef_)
print(model.intercept_)

