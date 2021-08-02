import math

class calc:
    def __init__(self):
        self.result = 0
    def add(a,b):
        self.result += float(b)
        return self.result
    
    def minus(a,b):
        self.result -= float(b)
        return self.result
    
    def c_(self):
        self.result = 0
        return 0
    
    def mult(a,b):
        self.result *= float(b)
        return self.result
    
    def div(a,b):
        self.result /= float(b)
        return self.result
    
    def squared(a,b):
        self.result **= b
        return self.result
    
    def fabs(a):
        return math.fabs(self.result)
    
    def fac(a):
        return math.factorial(self.result)
    
    def log10(a):
        return math.log10(self.result)
    
    def log2(a):
        return math.log2(self.result)
    
    def sqrt(a):
        return math.sqrt(self.result)
    
    def sin(a):
        return sin(self.result)
    
    def cos(a):
        return cos(self.result)
    
    def tan(a):
        return tan(self.result)
    
    def cir_area(a):
        return math.pi*(self.result**2)
    
    def cir_round(a):
        return math.pi*2*self.result
    
    def phrase_volume(a):
        return math.pi*(4/3)*(self.result**3)
    
    def phrase_surface_area(a):
        return math.pi*4*(self.result**2)
