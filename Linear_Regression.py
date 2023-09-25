from sympy import *
import time

class LR:
    def __init__(self,x,y,dimension):
        self.y = y
        self.x = x
        self.dimension = dimension-1
        self.m = [1 for i in range(self.dimension)]
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


    
# area, window, door
x = [[300,4,2],[400,3,1],[700,5,3],[1000,3,2],[1300,7,4],[1450,3,3],[1500,1,1],[1700,5,3]]
y = [100,110,150,165,230,220,200,260]





model = LR(x,y,4)
# print(model.GD(100,out=True))
# print(model.SSE())
print(model.predict([4000,10,8],custom=True,m_l = [0.10518191, 7.94595549,0.28735429],b_l = 38.11833274461321))