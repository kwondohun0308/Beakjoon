N = int(input())

def binary(n):
    if n == 0:
        return n
    else:
        binary(n//2)
        print(n%2, end = '')

binary(N)
