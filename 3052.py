a = []
arr = []
count = 0
for i in range(10):
    a.append(int(input()))
    a[i] = a[i] % 42
a = set(a)
print(len(a))
