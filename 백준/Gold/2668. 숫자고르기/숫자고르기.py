# Cycle을 탐지하는 문제


def dfs(start,now):
    visited[now] = True

    for next in graph[now]:
        if not visited[next]:
            return dfs(start,next)
        if next == start:
            return True

    return False

N = int(input())

graph = [[] for i in range(N + 1)]
for i in range(1,N+1):
    graph[i].append(int(input()))


cnt =0
cycle = []
for i in range(1,N+1):
    visited = [False] * (N + 1)
    if dfs(i,i):
        cycle.append(i)
        cnt += 1

print(cnt)
for i in cycle:
    print(i)