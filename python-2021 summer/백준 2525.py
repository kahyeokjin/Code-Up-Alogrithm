hour,minute=map(int,input().split())
cook=int(input())

hour+=cook//60
minute+=cook%60


if minute >= 60:
    hour += 1
    minute -= 60
if hour >= 24:
    hour -= 24


print("%d %d"%(hour,minute))
    
