avg = 0
for i in range(5):
    a = int(input())
    if a < 40:
        a = 40
    else:
        pass
    avg += a
print(int(avg / 5))
