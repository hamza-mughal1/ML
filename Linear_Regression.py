from sympy import *

class LR:
    def __init__(self,x,y,dimension):
        self.y = y
        self.x = x
        self.dimension = dimension-1
        self.m = [1 for i in range(dimension)]
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

    def GD(self,loops):
        l_r = 0.01
        for _ in range(loops):
            for i in range(self.dimension):
                slope = self.derivative(f"m{i}")
                step = slope*l_r
                self.m[i] += step
            
            slope = self.derivative("b")
            step = slope*l_r
            self.b += step 

            l_r = l_r/1.0001

        return
    
    def predict(self,value):
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


    
x = [[2,2],[5,5],[1,1],[3,3],[4.5,4.5]]
y = [2.5,4.8,0.9,3.3,4.1]

model = LR(x,y,3)
print(model.SSE())
print(model.GD(100))
print(model.SSE())
print(model.predict([2,2]))