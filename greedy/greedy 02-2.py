n,m,k=map(int,input().split())
numbers=list(map(int,input().split()))

numbers.sort()
first=numbers[n-1]
second=numbers[n-2]

count=int(m/(k+1))*k
count+=m%(k+1)

result=0
result+=count*first
result+=(m-count)*second

print("큰수의 법칙에 의해 정답은 %d입니다."%result)
