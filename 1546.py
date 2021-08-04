avg = 0
a = int(input())
arr = list(map(int, input().split()))
M = max(arr)
arr = sorted(arr)
for i in range(a):
    arr[i] = arr[i] / M * 100
    avg += arr[i]
avg = avg / a
print(avg)
