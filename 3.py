ID = "ai_cprog"
PW = "12345"
print("C world system.")
T = 0
Try = 0
A = input("ID : ")
if A == ID:
    pass
else:
    T = 1
    print("ID가 틀렸습니다. 프롬프트을 종료합니다")
if T == 0:
    for i in range(3):
        B = input("Password : ")
        if B == PW:
            print("Welcome to C world.\n")
            break
        else:
            print("비밀번호가 틀렸습니다. 다시 입력하시오.")
            Try += 1
        if Try == 3:
            print("비밀번호 3회를 모두 틀리셨습니다. 프롬프트를 종료합니다.")      
            break
