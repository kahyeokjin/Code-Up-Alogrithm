import random


def make_question():
    num1 = random.randint(1,40)
    num2 = random.randint(1,50)
    op = random.randint(1,3)

    q=str(num1)

    if op == 1:
        q=q+"+"
    if op == 2:
        q=q+"-"
    if op == 3:
        q=q+"*"

    q=q+str(num2)

    return q

sc1 =0
sc2 =0
sc3=input("문제숫자를 입력하시오")
sc4=int(sc3)
for x in range(sc4):
    q=make_question()
    print(q)
    ans=input("=")
    r= int(ans)

    if eval(q)==r:
        print("정답")
        sc1=sc1+1
    else:
        print("오답")
        sc2=sc2+1
print ("정답수",sc1,"오답수",sc2)
if sc2==0:
    print("만점입니다.")
