A = int(input())
B = int(input())
C = int(input())
D = A * B * C
D = str(D)
D = list(D)
for i in range(10):
    print(list(D).count(str(i)))
