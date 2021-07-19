hour,minute,second=map(int,input().split())
cook=int(input())


second += cook % 60
cook = cook // 60


if second >=60:
    second -= 60
    minute += 1

minute += cook % 60
cook = cook // 60
if minute >= 60:
    hour += 1
    minute -= 60

hour += cook %24
if hour >= 24:
    hour -= 24


print("%d %d %d"%(hour,minute,second))
