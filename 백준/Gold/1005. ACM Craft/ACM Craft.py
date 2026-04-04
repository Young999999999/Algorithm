from collections import deque

t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    time = list(map(int,input().split()))
    time.insert(0,0)
    graph = [[] for i in range(n+1)]
    indegree = [0] * (n+1)
    q = deque()

    for __ in range(k):
        x,y = map(int,input().split())
        indegree[y] += 1
        graph[x].append(y)

    cost = [0] * (n + 1)

    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)
            cost[i] = time[i]

    while q:
        now = q.popleft()
        c = cost[now]

        for next in graph[now]:
            indegree[next] -= 1

            cost[next] = max(cost[next], time[next] + c)
            if indegree[next] == 0:
                q.append(next)

    target = int(input())
    print(cost[target])




