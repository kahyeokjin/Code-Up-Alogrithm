numList=[]
for i in range(10):
    num=int(input)
    numList.append(int(num%42))
numList=set(numList)
print(len(numList))
