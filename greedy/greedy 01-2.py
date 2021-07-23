N=int(input())

count=0

coins=[500,100,50,10]

for coin in coins:
    count += N // coin
    N=N%coin
print("최소 동전의 수는 %d입니다."%count)
