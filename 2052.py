N=int(input())
a=1
for i in range(N):
    a = a / 2
a = '%.250f'%a
length = len(a)
for i in range(length-1,0,-1):
    if a[i] != '0':
        length = i
        break
print(a[:length+1])
