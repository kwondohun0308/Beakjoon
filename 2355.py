A,B=map(int, input().split())
large=max(A,B)
small=min(A,B)
s=(large + small)/2 * (large + 1 - small)
print(int(s))
