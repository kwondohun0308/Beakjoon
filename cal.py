import math

def add(a,b):
    return a+b
def minus(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    return a/b
def squared(a,b):
    return a**b
def fabs(a):
    return math.fabs(a)
def fac(a):
    return math.factorial(a)
def log10(a):
    return math.log10(a)
def log2(a):
    return math.log2(a)
def sqrt(a):
    return math.sqrt(a)
def sin(a):
    return sin(a)
def cos(a):
    return cos(a)
def tan(a):
    return tan(a)
def quad_formula(a,b,c):
    D = b**2 - 4*a*c
    if D < 0:
        return 0
    x_1 = (-b + math.sqrt(b*b - 4*a*c))/2*a
    x_2 = (-b - math.sqrt(b*b - 4*a*c))/2*a
    elif D = 0:
        return x_1
    else:
        return x_1, x_2
def cir_area(a):
    return math.pi*(a**2)
def cir_round(a):
    return math.pi*2*a
def phrase_volume(a):
    return math.pi*(4/3)*(a**3)
def phrase_surface_area(a):
    return math.pi*4*(a**2)

arr = list(map(str, input().split()))
result = arr[0]
for i in range(1,len(arr)):
    if arr[i] == '+':
        i+=1
        result = add(result, arr[i])
        
    if arr[i] == '-':
        i+=1
        result = minus(result, arr[i])
        
    if arr[i] == '*':
        i+=1
        result = mult(result, arr[i])
        
    if arr[i] == '/':
        i+=1
        result = div(result, arr[i])
        
    if arr[i] == '!':
        i+=1
        result = fac(result, arr[i])
        
    if arr[i] == '||':
        i+=1
        result = fabs(result, arr[i])
        
    if arr[i] == 'log10':
        i+=1
        result = log10(result, arr[i])
        
    if arr[i] == 'log2':
        i+=1
        result = log2(result, arr[i])
        
    if arr[i] == 'root':
        i+=1
        result = sqrt(result, arr[i])
        
    if arr[i] == 'sin':
        i+=1
        result = sin(result, arr[i])
        
    if arr[i] == 'cos':
        i+=1
        result = cos(result, arr[i])
        
    if arr[i] == 'tan':
        i+=1
        result = tan(result, arr[i])
        
    if arr[i] == 'quad_formula':
        i+=1
        result = quad_formula(result, arr[i])
    
    if arr[i] == 'cir_area':
        i+=1
        result = cir_area(result, arr[i])

    if arr[i] == 'cir_round':
        i+=1
        result = cir_round(result, arr[i])

    if arr[i] == 'phrase_volume':
        i+=1
        result = phrase_volume(result, arr[i])

    if arr[i] == 'phrase_surface_area':
        i+=1
        result = phrase_surface_area(result, arr[i])
        
    if arr[i] == 'squared':
        i+=1
        result = squared(result, arr[i])

print(result)
