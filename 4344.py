T = int(input())

for i in range(T):
    arr = list(map(int, input().split()))
    avg = (sum(arr) - arr[0]) / arr[0]
    count = 0
    for j in range(1,arr[0]+1):
        if arr[j] > avg:
            count += 1
    print('{:.3f}%'.format(count/arr[0]*100))
