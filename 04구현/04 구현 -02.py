n=int(input())

count=0
for i in range(n+1):
    for a in range(60):
        for b in range(60):
            if '3' in str(i)+str(a)+str(b):
                count +=1

print (count)
