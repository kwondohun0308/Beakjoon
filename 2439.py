a=int(input())
for i in range(a):
    b = a - (i+1)
    for j in range(a):
        if b > 0:
            print(' ',end='')
        else:
            print('*',end='')
        b-=1
    print()
