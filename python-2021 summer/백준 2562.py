numList=[]
for i in range(9):
    numList.append(int(input()))
print(max(numList),numList.index(max(numList))+1,sep="\n")
