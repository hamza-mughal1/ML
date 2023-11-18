import numpy as np
from  matplotlib import pyplot as plt
from collections import Counter
import operator
import ast

"""default dataset"""
dataset = {"blue":[[2,3,1],[2,4,1],[1,5,2],[1,4,3],[2,5,3],[3,3,2],[3,4,4],[3,5,4]],
           "red":[[5,0,4],[5,1,4],[5,2,5],[6,0,6],[6,1,6],[6,2,5],[7,0,7],[7,1,7],[7,2,6]]}

"""default point for prediction"""
test_point = [5,4,7]

"""defining global function"""
def convert_string_list(input_string):
    """function converts user input point into list"""
    # Remove the first and last characters (square brackets)
    input_string = input_string[1:-1]

    # Convert the string into a list
    output_list = ast.literal_eval(input_string)

    return list(output_list)

""""KNN class"""
class KownNearestNeighbor:
    def __init__(self,k=3):
        self.k = k
        self.points = None

    def fit(self,points):
        self.points = points

    def euclidean_distance(self,p,q):
        return np.sqrt(np.sum((np.array(p) - np.array(q))**2))
    
    def predict(self,new_point):
        distance = []
        neighbors = []
        for key, values in dataset.items():
            for point in values:
                distance.append((key,self.euclidean_distance(point,new_point)))

        distance = sorted(distance, key=operator.itemgetter(1))
        neighbors = [i[0] for i in distance[:self.k]]
        return Counter(neighbors).most_common(1)[0][0]

"""main block"""
if __name__ == "__main__":

    user_test_point = input("enter your point for prediction (for default press 'enter') : ")
    if user_test_point:
        test_point = convert_string_list(user_test_point)

    # initializing model
    model = KownNearestNeighbor(k=3)
    model.fit(dataset)

    # predicting point
    predicted = model.predict(test_point)
    print(predicted)

    # vitualizing 3d graph using matplotlib
    fig = plt.figure(figsize = (15,12))
    ax = fig.add_subplot(projection="3d")
    ax.grid(True,color="#323232")
    ax.set_facecolor("black")
    ax.figure.set_facecolor("#121212")
    ax.tick_params(axis="x",color="white")
    ax.tick_params(axis="y",color="white")

    for point in dataset["blue"]:
        ax.scatter(point[0], point[1], point[2], color="#104DCA", s=60)
    for point in dataset["red"]:
        ax.scatter(point[0], point[1], point[2], color="#FF0000", s=60)

    color = "#FF0000" if predicted == "red" else "#104DCA"
    ax.scatter(test_point[0], test_point[1], test_point[2], color=color, marker="*",s=200,zorder=100)

    for point in dataset["blue"]:
        ax.plot([test_point[0], point[0]], [test_point[1], point[1]],[test_point[2], point[2]], color="#104DCA",linewidth=1)
    for point in dataset["red"]:
        ax.plot([test_point[0], point[0]], [test_point[1], point[1]],[test_point[2], point[2]], color="#FF0000",linewidth=1)

    plt.show()