import sys
sys.setrecursionlimit(10**6)

n,m,k = map(int,input().split())
child = list(map(int,input().split()))
graph = [[] for i in range(n+1)]
candy = []

def dfs(x):
    global cnt
    global sum
    sum += child[x-1]
    cnt += 1
    visited[x] = True

    for next in graph[x]:
        if not visited[next]:
            dfs(next)

for i in range(m):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

visited=[False] * (n+1)
for i in range(1,n+1):
    if not visited[i]:
        cnt = 0
        sum = 0
        dfs(i)
        candy.append((cnt,sum))

dp = {}

for w,v in candy:
    for item in sorted(dp.keys(),reverse= True):
        idx = item + w
        if idx < k :
            if idx in dp:
                dp[idx] = max(dp[item] + v,dp[idx])
            else:
                dp[idx] = dp[item] + v

    if w in dp:
        dp[w] = max(dp[w],v)
    else:
        dp[w] = v

result = 0
for key in dp.keys():
    if key < k:
        result = max(result,dp[key])

print(result)


