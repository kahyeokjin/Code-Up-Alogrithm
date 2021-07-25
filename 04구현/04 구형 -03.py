pos=input()
row=int(pos[1])
col=int(ord(pos[0]))-int(ord('a'))+1

moves=[(-2,1),(2,1),(2,-1),(-2,-1),(1,2),(-1,-2),(-1,2),(1,-2)]

result=0

for move in moves:
    nrow=row+move[0]
    ncol=col+move[1]
    if nrow >= 1 and nrow <= 8 and ncol >= 1 and ncol <= 8:
        result += 1
print(result)
