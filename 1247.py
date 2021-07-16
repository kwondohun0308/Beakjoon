import sys
for i in range(3):
    a=int(sys.stdin.readline())
    s=0
    for i in range(a):
        b=int(sys.stdin.readline())
        s += b
    if s == 0:
        print('0')
    elif s < 0:
        print('-')
    else:
        print('+')
