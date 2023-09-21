import matplotlib.pyplot as plt
import time

class LR:
    def __init__(self,data):
        self.data = data
        self.m = 1
        self.b = 1

    def SSE(self):
        error = 0
        for i in self.data:
            error += (i[1]-(self.m*i[0]+self.b))**2

        return error
    
    def der_m(self):
        der = 0
        for i in self.data:
            der += (2*i[0])*(self.m*i[0]-i[1]+self.b)

        return der
    
    def der_b(self):
        der = 0
        for i in self.data:
            der += 2*(self.b-i[1]+self.m*i[0])

        return der

    def GD(self,loops):
        l_r = 0.01
        for _ in range(loops):
            dr_m = self.der_m()
            dr_m *= l_r
            self.m -= dr_m

            dr_b = self.der_b()
            dr_b *= l_r
            self.b -= dr_b

            l_r = l_r/1.001
        return (f"\n{self.m}\n{self.b}\n")
    

model = LR([(2,2.5),(5,4.8),(1,0.9),(3,3.3),(4.5,4.1)])
print(model.SSE())
print(model.GD(10000))
print(model.SSE())