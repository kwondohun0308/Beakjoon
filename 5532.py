L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
for a in range(100):
    if C * a >= A:
        break
    else:
        pass

for b in range(100):
    if D * b >= B:
        break
    else:
        pass
L_1 = L - a
L_2 = L - b

if L_1 < L_2:
    print(L_1)
else:
    print(L_2)
