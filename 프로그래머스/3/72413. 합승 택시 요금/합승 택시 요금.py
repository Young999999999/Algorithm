import heapq

def solution(n, s, a, b, fares):
    answer = int(1e9)
    graph = [[] for i in range(n+1)]
    for start,e,cost in fares:
        graph[start].append((e,cost))
        graph[e].append((start,cost))
    
    def dijkstra(s,e):
        INF = int(1e9)
        distance = [INF] * (n+1)
        distance[s] = 0
        q = []
        heapq.heappush(q, (0,s))
        
        while q:
            dist, now = heapq.heappop(q)
            
            if distance[now] < dist:
                continue
            
            for next, cost in graph[now]:
                
                if distance[next] > dist + cost:
                    distance[next] = dist + cost
                    heapq.heappush(q, (dist+cost, next))
        
        return distance[e]
                
    print(s,a)            
    print(dijkstra(s,a))
    
    for i in range(1, n+1):
        # 경유지까지의 비용
        cost = dijkstra(s,i)
        cost += dijkstra(i,a)
        cost += dijkstra(i,b)
        
        answer = min(answer,cost)
        
        
    
    return answer