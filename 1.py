from random import randrange

W = 0
D = 0
L = 0

for i in range(10):
    you = int(input("0,1,2(가위, 바위, 보) 중 하나를 입력하시오"))
    com = randrange(3)
    if you == 0:
        if com == 0:
            D += 1
            print('비깄으')
        elif com == 1:
            L += 1
            print('니는 졌으')
        else:
            W += 1
            print('이깄으')
    if you == 1:
        if com == 0:
            W += 1
            print('이깄으')
        elif com == 1:
            D += 1
            print('비깄으')
        else:
            L += 1
            print('니는 졌으')
    if you == 2:
        if com == 0:
            L += 1
            print('니는 졌으')
        elif com == 1:
            W += 1
            print('이깄으')
        else:
            D += 1
            print('비깄으')
            
print('당신의 승률은',int((W/10)*100),'%이며, 당신은',L,'번 졌고,',D,'번 비기셨습니다.')
