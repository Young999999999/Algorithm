N,M,X = map(int,input().split())
import sys
sys.setrecursionlimit(10**6)

def DFS(X):
    global outDegree
    outDegree += 1
    visited[X] = True

    for i in graph[X]:
        if not visited[i] :
            DFS(i)


def DFS2(X):
    global outDegree2
    outDegree2 += 1
    visited[X] = True

    for i in graph2[X]:
        if not visited[i] :
            DFS2(i)


outDegree = 0
outDegree2 = 0

graph = [[] for i in range(N+1)]
graph2=[[] for i in range(N+1)]
visited= [False] * (N+1)

candidate = [False] * (N+1)
candidate[X] = True

for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)

    if candidate[b] :
        graph2[b].append(a)
        candidate[a] = True

DFS(X)
DFS2(X)
print(outDegree2,N - outDegree + 1)
