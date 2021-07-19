a,b,c,d = map(int, input().split())
S = a+b+c+d
e,f,g,h = map(int, input().split())
T = e+f+g+h
if S>=T:
    print(S)
else:
    print(T)
