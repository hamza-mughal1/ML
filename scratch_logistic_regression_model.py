import sympy as sp
import math

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
            func = 1/1+e**-b
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

    def GD(self,loops,out=False):
        l_r = 0.0005
        for o in range(loops):
            print(o)
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

    
model = LogReg([[3,1,8,220,6],[4.5,2.3,11,234,7],[2,0.5,6,160,4],[6,3,13,240,8],[2,1,8,200,6],[3.5,1.3,9,190,7]],[0,1,0,1,1,1],6)

print(model.LogLoss())
print(model.GD(100,out=True))
print(model.LogLoss())

# print(model.predict([3,1,5,140,4]))
# print(model.predict([3,1,5,140,4],custom=True,m_l=[-0.696665525399225, 0.267000493054445, -3.44666367560425, -99.7865988722415, -2.09666458368542],b_l=0.510000329599827))



