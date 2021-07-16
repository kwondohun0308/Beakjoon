prize=0
a,b,c=map(int,input().split())
if a==b==c:
    prize = a * 1000 + 10000
elif a==b or a==c:
    prize = a * 100 + 1000
elif b==c:
    prize = b * 100 + 1000
else:
    if a>b and a>c:
        prize = a * 100
    elif b>a and b>c:
        prize = b * 100
    else:
        prize = c * 100
print(prize)
