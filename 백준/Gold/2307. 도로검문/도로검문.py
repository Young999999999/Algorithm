import heapq
import sys
input = sys.stdin.readline
def make_short_route(seed):
    if route[seed]:
        short_route.append(route[seed])
        make_short_route(route[seed])

def dijkstra(a,b,start): # a와 b를 잇는 도로를 막는다고 가정하자
    q=[]
    heapq.heappush(q,(0,start)) #start에서 start의 cost는 0이므로 0,start push
    distance[start] = 0
    while q:
        dist,now=heapq.heappop(q) #현재까지 알려진 cost비용 dist 와 현재의 노드 now

        if dist > distance[now]: #이미 distance[now]가 밝혀졌다면
            continue

        for i in graph[now]:
            if a==now or b==now : #a와 b를 잇는 도로는 막혀있다.
                if a == i[0] or b== i[0]:
                    continue

            if distance[i[0]] > dist+i[1] :
                distance[i[0]] = dist+i[1]
                heapq.heappush(q,(distance[i[0]],i[0]))
                route[i[0]] = now
    return now
INF = int(1e9)

n,m = map(int,input().split())
start= 1
distance=[INF]*(n+1)
graph = [[]for i in range(n+1)]
route = [0]*(n+1)
road = []
short_route=[]

for i in range(m): #모든 도로를 다 하니까 시간초과가 뜨는 것 같음 최단 거리의 경로를 알고 그 경로에 해당할 때만 다시 다익스트라 하자
    a,b,c = map(int,input().split())
    if b==n:
        road.append((a,b))
    graph[a].append((b,c))
    graph[b].append((a,c))

dijkstra(0,0,start)
if distance[n] == INF:
    print(-1)
    exit(0)
nonblock = distance[n]
block = []

make_short_route(n)
short_route.reverse()
short_route.append(n)

for i in range(len(short_route)-1):
    distance=[INF] * (n+1)
    dijkstra(short_route[i],short_route[i+1],start)
    block.append(distance[n])
    if distance[n] == INF :
        print(-1)
        exit(0)


result=-1
for i in block:
    if i-nonblock  > result:
        result =i-nonblock

print(result)

"""
6 6
1 2 1
2 3 1
3 4 1
4 5 1
5 6 1
2 6 2
"""