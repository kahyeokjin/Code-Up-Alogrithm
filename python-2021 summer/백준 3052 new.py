numList[]
for i in range(10):
    num=int(input)
    numList.append(num%42)
numList=set(numList)
print(len(numList))
