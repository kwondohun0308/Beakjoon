m,n = map(int, input().split())
if n <= 1:
    print('소수는 없습니다.')
for i in range(m,n+1):
    count = 0
    for j in range(1,i+1):
        if i<2:
            count = 3
        if i%j==0:
            count += 1
    if count <= 2:
        print(i)
