T = int(input())

for i in range(T):
    a,b=map(int,input().split())
    c=a+b
    print("Case #%s: %s + %s = %s"%(i+1,a,b,c))
