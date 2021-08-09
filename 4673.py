def d(n):
    n = n + sum(map(int, str(n)))

    return n
a = []
for i in range(1,10001):
    k = d(i)
    a.append(k)

for j in range(1, 10001):
    if j in a:
        pass
    else:
        print(j)
