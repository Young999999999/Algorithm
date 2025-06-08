import sys
sys.setrecursionlimit(int(1e7))
input = sys.stdin.readline

def isIndegreeZero():
    idx = []
    for i in range(n):
        if indegree[i] == 0:
            idx.append(i)
            indegree[i] = -1

    return idx
def dfs(cur,t):
    t += time[cur-1]

    arrive[cur] = max(t,arrive[cur])

    for next in graph[cur]:
        arrive[next] = max(arrive[next], arrive[cur]+ time[next - 1])
        indegree[next-1] -= 1
        if indegree[next-1] == 0 :
            dfs(next,t)

T = int(input())

for i in range(T):
    n,k = map(int,input().split())
    time = list(map(int,input().split()))
    arrive=[0] * (n+1)
    indegree = [0] * n
    graph=[[] for i in range(n+1)]
    pre= []
    for i in range(k):
        x,y = map(int,input().split())
        indegree[y-1] += 1
        graph[x].append(y)

    w = int(input())

    start = isIndegreeZero()

    for i in start:
        dfs(i+1,0)

    for s in range(1,n+1):
        for e in graph[s]:
            if e==w:
                pre.append(s)
                break
    
    print(arrive[w])


