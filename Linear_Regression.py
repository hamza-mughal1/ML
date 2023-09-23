from sympy import *
import time

class LR:
    def __init__(self,x,y,dimension):
        self.y = y
        self.x = x
        self.dimension = dimension-1
        self.m = [1 for _ in range(self.dimension)]
        self.b = 1

    def equation(self,x):
        num = 0
        for pos,i in enumerate(x):
            num += self.m[pos]*i
        num+=self.b
        return num

    def SSE(self):
        error = 0
        for i in range(len(self.x)):
            error += (self.y[i]-(self.equation(self.x[i])))**2

        return error
    
    def derivative(self,subject):
        dr = 0
        for pos,i in enumerate(self.x):
            e = symbols("b")
            e = -e
            e += symbols("y")
            for j in range(self.dimension):
                m = symbols(f"m{j}")
                x = symbols(f"x{j}")
                e += -m*x
            e = e**2
            r = symbols(subject)
            e = diff(e,r)
            subss = {"b":self.b,
                    "y":self.y[pos]}
            for j in range(self.dimension):
                subss[f"m{j}"]=self.m[j]
                subss[f"x{j}"]=i[j]

            dr += e.subs(subss)
    
        return dr

    def GD(self,loops,out=False):
        l_r = 0.00000005
        for _ in range(loops):
            for i in range(self.dimension):
                slope = self.derivative(f"m{i}")
                step = slope*l_r
                self.m[i] -= step
            
            slope = self.derivative("b")
            step = slope*l_r
            self.b -= step 

            l_r = l_r/1.01
        if out == True:
            return (self.m,self.b)
        return
    
    def predict(self,value,custom=False,m_l = None,b_l = None):
        if custom == True:
            e = symbols("b")
            for j in range(self.dimension):
                m = symbols(f"m{j}")
                x = symbols(f"x{j}")
                e += m*x

            subss = {"b":b_l}
            for j in range(self.dimension):
                subss[f"m{j}"]=m_l[j]
                subss[f"x{j}"]=value[j]

            return e.subs(subss)
        elif custom == False:
            e = symbols("b")
            for j in range(self.dimension):
                m = symbols(f"m{j}")
                x = symbols(f"x{j}")
                e += m*x

            subss = {"b":self.b}
            for j in range(self.dimension):
                subss[f"m{j}"]=self.m[j]
                subss[f"x{j}"]=value[j]

            return e.subs(subss)


    
x = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20], [21], [22], [23], [24], [25], [26], [27], [28], [29], [30], [31], [32], [33], [34], [35], [36], [37], [38], [39], [40], [41], [42], [43], [44], [45], [46], [47], [48], [49], [50], [51], [52], [53], [54], [55], [56], [57], [58], 
[59], [60], [61], [62], [63], [64], [65], [66], [67], [68], [69], [70], [71], [72], [73], [74], [75], [76], [77], [78], [79], [80], [81], [82], [83], [84], [85], [86], [87], [88], [89], [90], [91], [92], [93], [94], [95], [96], [97], [98], [99], [100]]

y = [0.822, 1.999, 3.14, 4.129, 5.169, 5.767, 7.297, 7.872, 9.282, 9.75, 11.074, 11.968, 12.999, 14.072, 14.729, 15.851, 17.006, 18.258, 19.118, 20.185, 20.785, 22.021, 23.19, 23.738, 24.744, 26.143, 27.083, 28.189, 28.71, 30.06, 30.8, 32.169, 33.018, 34.021, 34.983, 36.034, 36.984, 37.808, 39.192, 39.776, 40.819, 41.863, 42.812, 43.996, 45.126, 45.83, 46.719, 47.728, 48.829, 50.071, 50.826, 51.783, 53.094, 53.935, 
55.204, 55.991, 56.831, 57.844, 58.757, 60.026, 60.868, 62.003, 63.031, 63.942, 65.072, 66.066, 66.826, 
68.179, 68.763, 69.861, 70.914, 72.014, 72.744, 73.758, 74.788, 76.005, 76.823, 77.897, 79.001, 80.113, 
80.729, 82.056, 83.095, 84.113, 84.865, 86.035, 86.948, 88.039, 89.066, 89.855, 91.27, 91.959, 93.275, 93.889, 95.226, 95.87, 97.201, 97.963, 99.03, 100.071]

model = LR(x,y,2)
# print(model.SSE())
# print(model.predict([1001]))
# start = time.time()
# print(model.GD(100,out=True))
# end = time.time()
# print("time : ",end-start)
# print(model.SSE())
print(model.predict([1001],custom=True,m_l = [0.986386645441406],b_l = 0.999641751671971))