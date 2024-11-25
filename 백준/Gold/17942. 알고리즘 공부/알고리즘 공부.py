import heapq
import sys
input= sys.stdin.readline
q = []
N,M = map(int,input().split())
algorithms= list(map(int,input().split()))
r = int(input())
graph = [[] for i in range(N)]
visited=[False] * (N)
for i in range(r):
    a,b,c = map(int,input().split())
    graph[a-1].append((b-1,c))

cnt = 0
for idx,value in enumerate(algorithms):
    heapq.heappush(q,(value,idx))

#이미 방문했으면 continue
# 방문 안했으면 graph 돌면서 값 빼주고 visited 처리
result = 0
while cnt<M:
    value,idx = heapq.heappop(q)
    #print(value,idx)
    if not visited[idx]:
        for next,c in graph[idx]:
            algorithms[next] -= c
            heapq.heappush(q,(algorithms[next],next))

        visited[idx] = True
        cnt += 1
        result = value

print(result)





