import sympy as sp
import math
from matplotlib import pyplot as plt
import time
import random

class LogReg:
    eular = 2.71828
    def __init__(self,x,y,dimension):
        self.x = x
        self.y = y 
        self.dimension = dimension -1 
        self.m = [1 for _ in range(self.dimension)]
        self.b = 1


    def equation(self,x):
        num = 0
        for pos,i in enumerate(x):
            num += self.m[pos]*i
        num+=self.b
        
        sigmoid = 1/(1+LogReg.eular**-(num))
        return sigmoid

    def LogLoss(self):
        error = 0
        for pos,i in enumerate(self.x):
            eq = self.equation(i) - 1e-15
            if eq >= 1:
                error += self.y[pos]*math.log(eq)
            elif eq < 1:
                error += (1-self.y[pos])*math.log(1-eq)
        
        error = -(1/len(self.x))*error
        return error
    
    def derivative(self,subject):
        dr = 0
        for pos,i in enumerate(self.x):
            e = sp.symbols("e")
            b = sp.symbols("b")
            
            for j in range(self.dimension):
                m = sp.symbols(f"m{j}")
                x = sp.symbols(f"x{j}")
                b += m*x
            func = 1/(1+e**-b)
            y = sp.symbols("y")
            summ = (y*sp.log(func)+(1-y)*sp.log(1-func))

            r = sp.symbols(subject)
            summ = sp.diff(summ,r)
        
            subss = {"b":self.b,
                    "y":self.y[pos],
                    "e":LogReg.eular}
            for j in range(self.dimension):
                subss[f"m{j}"]=self.m[j]
                subss[f"x{j}"]=i[j]

            dr += summ.subs(subss)
    
        return -(dr/len(self.x))
    
    def plotting(self):
        y = []
        x = []
        for i in self.x:
            x.append(i[0])

        x.sort()
        for i in x:
            f = 1/(1+(2.71828)**-(self.m[0]*i+self.b))
            y.append(f)

        plt.plot(x,y)

        plt.xlabel("x value")
        plt.ylabel("y value")

        plt.show()

    def GD(self,loops,out=False):
        l_r = 0.0005
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
            e = sp.symbols("e")
            b = sp.symbols("b")
            
            for j in range(self.dimension):
                m = sp.symbols(f"m{j}")
                x = sp.symbols(f"x{j}")
                b += m*x
            func = 1/(1+e**-b)

            subss = {"b":b_l,
                     "e":LogReg.eular}
            for j in range(self.dimension):
                subss[f"m{j}"]=m_l[j]
                subss[f"x{j}"]=value[j]

            return func.subs(subss)
        elif custom == False:
            e = sp.symbols("e")
            b = sp.symbols("b")
            
            for j in range(self.dimension):
                m = sp.symbols(f"m{j}")
                x = sp.symbols(f"x{j}")
                b += m*x
            func = 1/(1+e**-b)

            subss = {"b":self.b,
                     "e":LogReg.eular}
            for j in range(self.dimension):
                subss[f"m{j}"]=self.m[j]
                subss[f"x{j}"]=value[j]

            return func.subs(subss)

    
model = LogReg([[3,2,6,150,4],[4.5,3,7,190,7],[2,1,3,130,3],[6,4,13,240,8],[3,3,9,180,6],[3.5,2.2,8,185,7]],[0,1,0,1,1,1],6)

print(model.LogLoss())
print(model.GD(100,out=True))
print(model.LogLoss())
