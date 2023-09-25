import matplotlib as plt
import numpy as np
from sklearn import linear_model,datasets
from sklearn.metrics import mean_squared_error


house_price_x_train = np.array([[300,4,2],[400,3,1],[700,5,3],[1000,3,2],[1300,7,4],[1450,3,3],[1500,1,1],[1700,5,3]])

house_price_y_train = [100,110,150,165,230,220,200,260]

model = linear_model.LinearRegression()

model.fit(house_price_x_train,house_price_y_train)

house_price_y_predict = model.predict(np.array([[4000,10,8]]))

print(house_price_y_predict)
print(model.coef_)
print(model.intercept_)


