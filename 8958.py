a = int(input())
for i in range(a):
    arr_1 = list(input())
    S = 0
    start = 1
    for j in arr_1:
        if j == 'O':
            S += start
            start += 1
        else:
            start = 1
    print(S)
