S = 0
arr = list(map(int, input().split()))
for i in arr:
    S += i ** 2
S = S % 10
print(S)
