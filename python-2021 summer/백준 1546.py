N= int(input())
scoreList=list(map(int,input().split()))
scoreMax=max(scoreList)

for i in range(N):
    scoreList[i]=scoreList[i]/scoreMax*100

avgScore=sum(scoreList)/N
print("%.2f"%avgScore)    
