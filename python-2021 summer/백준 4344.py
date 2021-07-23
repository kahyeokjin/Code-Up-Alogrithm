C = int(input())

for i in range(C):
    score = list(map(int,input().split()))
    avg=sum(score[1:])/score[0]
    n=0
    for k in score:
        if k>avg:
            n+=1
    percent=n/score[0]
    print("%.3f"%(percent*100))
            
