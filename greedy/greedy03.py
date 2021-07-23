n,m=map(int,input().split())

answer=0
for i in range(n):
    cards=list(map(int,input().split()))
    minvalue=min(cards)
    answer=max(answer,minvalue)
print(answer)
    
