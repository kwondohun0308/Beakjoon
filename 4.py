try:
    f = open("fruit.txt", "r")
    a = int(f.readline())
    o = int(f.readline())
    g = int(f.readline())
    f.close()
except:
    a,o,g = 0,0,0
    
while True:
    print("현재 재고는 사과",a,"개, 오렌지",o,"개, 포도",g,"개 입니다.")
    S,t = input("변동할 재고와 갯수를 입력해주세요(저장하고 나갈때는 q 0 입력) : ").split()
    t = int(t)
    if S == 'apple' :
        a += t
    elif S == 'orange' :
        o += t
    elif S == 'grape' :
        g += t
    else:
        f = open("fruit.txt", "w")
        f.write(str(a))
        f.write('\n')
        f.write(str(o))
        f.write('\n')
        f.write(str(g))
        f.close()
        print('저장 완료')
        break
