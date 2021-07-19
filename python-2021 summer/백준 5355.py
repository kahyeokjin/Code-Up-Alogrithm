T=int(input())
for k in range(T):
    mars = list(map(str,input().split(" ")))
    answer = float(mars.pop(0))
    for i in mars:
        if i=='@':
            answer=answer*3
        elif i =='#':
            answer=answer-7
        elif i == '%':
            answer = answer +5
    print("%.2f"%(answer))
