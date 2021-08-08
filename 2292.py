N = int(input())

bee_nums = 1
count = 1

while N > bee_nums:
    bee_nums += 6 * count
    count += 1
print(count)
