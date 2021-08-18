count = 0
def my_len():
    while True:
        try:
            if a[count]:
                count += 1
        except:
            break
        
a = input("단어 길이를 알고싶은 단어를 입력하시오: ")
print(len(a))
print(my_len())
print(arr[::-1])
for i in range(len(a)):
        print(a[len(a)-i-1],end = '')
