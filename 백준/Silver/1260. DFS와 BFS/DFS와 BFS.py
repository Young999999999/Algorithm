import sys
from collections import deque
input =sys.stdin.readline

def dfs(v):
    # 방문 표시
    visited[v] = True
    print(v, end=' ')
    # 그래프를 순환하면서 인접 노드들을 방문
    for i in graph[v]:
        # 만약 방문하지 않은 노드가 있다면
        if not visited[i]:
            # 탐색 시작
            dfs(i)

def bfs(node):
    q=deque()
    q.append(node)
    while(q):
        x=q.popleft()
        visited[x] = True
        print(x, end=' ')

        for i in graph[x]:
            if not visited[i]:
                visited[i]=True
                q.append(i)
n,m,v = map(int,input().split())

graph=[[] for i in range(n+1)]
visited=[False]*(n+1)
for i in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in graph:
    i.sort()

dfs(v)
print()
visited=[False]*(n+1)
bfs(v)