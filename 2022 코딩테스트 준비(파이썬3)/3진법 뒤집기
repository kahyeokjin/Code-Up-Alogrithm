def solution(n):
    list=[]
    result=0
    while n>0:
        if n % 3 ==0:
            list.append(0)
        else:
            list.append(n%3)
        n=n//3
    listLength=len(list)
    t=0
    for i in range(listLength,0,-1):
        result+=((list[i-1])*(3**t))
        t+=1

    return result
    
