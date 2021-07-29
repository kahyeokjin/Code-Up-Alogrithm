from collections import deque

n,m,v=map(int,input().split())

graph=[[0]*(n+1)for _ in range(n+1)]

for _ in range(m):
    m1,m2=map(int,input().split())
    graph[m1][m2]=graph[m2][m1]=1


def dfs(v,discovered=[]):
    discovered.append(v)
    print(v, end=' ')
    for w in range(len(graph[v])):
        if graph[v][w]==1 and (w not in discovered):
            dfs(w,discovered)

def bfs(v):
    discovered=[v]
    queue=deque()
    queue.append(v)

    while queue:
        v=queue.popleft()
        print(v,end=' ')

        for w in range(len(graph[v])):
            if graph[v][w] == 1 and (w not in discovered):
                discovered.append(w)
                queue.append(w)


dfs(v)
print()
bfs(v)
