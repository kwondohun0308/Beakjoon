arr = []
for i in range(9):
    arr.append(int(input()))
               
t = max(arr)
print(t)
y = arr.index(t) + 1
print(y)
