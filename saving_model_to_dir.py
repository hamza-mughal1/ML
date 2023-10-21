import matplotlib as plt
import numpy as np
import pickle
import joblib
from sklearn import linear_model,datasets
from sklearn.metrics import mean_squared_error




house_price_x_train = np.array([[300,4,2],[400,3,1],[700,5,3],[1000,3,2],[1300,7,4],[1450,3,3],[1500,1,1],[1700,5,3]])

house_price_y_train = [100,110,150,165,230,220,200,260]

model = linear_model.LinearRegression()

model.fit(house_price_x_train,house_price_y_train)

"""using pickle for saving and accessing"""
with open ("model.pickle","wb") as f:
    pickle.dump(model,f)


with open ("model.pickle","rb") as f:
    mp = pickle.load(f)


mp.predict(np.array([[4000,10,8]]))

"""using joblib for saving and accessing"""

jb = joblib.dump(model,"model.joblib")

jb = joblib.load(model,"model.joblib")