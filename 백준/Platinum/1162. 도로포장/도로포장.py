import sys
import heapq
input = sys.stdin.readline
INF = int(1e11)
n,p,k = map(int,input().split())
graph = [[] for i in range(n+1)]
distance = [[INF for i in range(n+1)] for i in range(k+1)]

for i in range(k+1):
    distance[i][1] = 0

for i in range(p):
    s,e,c = map(int,input().split())
    graph[s].append((e,c))
    graph[e].append((s,c))

def dijkstra():
    q = []
    #초기값 설정
    global k
    #dist,now,k
    heapq.heappush(q,(0,1,k))

    while q:
        dist,now,k = heapq.heappop(q)

        if dist > distance[k][now]:
            continue

        for next,cost in graph[now]:

            if k>=1 and distance[k][now] < distance[k-1][next]:
                distance[k-1][next] = distance[k][now]
                heapq.heappush(q, (distance[k][now], next, k-1))
                #k를 소모함으로 비용이 0인채로 간다.

            if distance[k][now] + cost < distance[k][next]:
                distance[k][next] = distance[k][now] + cost
                heapq.heappush(q, (distance[k][now] + cost, next, k))

dijkstra()

answer= [0] * (k+1)
for i in range(k+1):
    answer[i] = distance[i][-1]

print(min(answer))
