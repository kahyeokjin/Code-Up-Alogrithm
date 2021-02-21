import random
import time

words = ["cat","cake","drink","snake","horse","pencil"]
n=1
print("아무키나 누르면 타자테스트를 시작합니다.")
input()
start=time.time()

q=random.choice(words)
while n <= 5:
    print("<문제>",q)
    x=input("정답")
    if q == x:
        print("통과")
        n=n+1
        q=random.choice(words)
    else:
        print("재도전")

end=time.time()
res=end-start
res=format(res,".2f")
print("총 걸린시간:",res,"초")
