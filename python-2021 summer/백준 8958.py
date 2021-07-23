N=int(input())
for i in range(N):
    testCase=list(map(str,input()))
    case=len(testCase)
    c=1
    sum =0
    for k in testCase:
        if k=='O':
            sum += c
            c +=1
        else:
            c=1
    print(sum)
            


        
