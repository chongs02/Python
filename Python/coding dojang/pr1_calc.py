from math import *

class Calc:
    def __init__(self, num):
        self.num = num
    
    def __add__(self, other):
        return self.num + other.num
    
    def __sub__(self, other):
        return self.num - other.num
    
    def __mul__(self, other):
        return self.num * other.num
    
    def __truediv__ (self, other):
        return self.num/other.num

class SCalc(Calc):
      
    def sin(self):
        return sin(self.num)
    
    def cos(self):
        return cos(self.num)
    
    def tan(self):
        return tan(self.num)

a = SCalc(1)
b = SCalc(2)
print('add',a+b)
print('sub',a-b)
print('mul',a*b)
print('div',a/b)

print('sin',a.sin())
print('cos',a.cos())
print('tan',a.tan())
