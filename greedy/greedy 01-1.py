N=int(input())

f=N//500
N=N-(500*f)

h=N//100
N=N-(100*h)

c=N//50
N=N-(50*c)

d=N//10
N=N-(10*d)

print(f+h+c+d)
