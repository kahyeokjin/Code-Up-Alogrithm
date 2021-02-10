import random

a=random.randint(1,30)
b=random.randint(1,30)

print(a,"+",b,"=")
x=input("정답을 입력하시오")
c=int(x)

if a+b==c:
    print("정답")
else:
    print("틀림")
