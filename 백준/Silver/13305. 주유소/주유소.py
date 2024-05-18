n=int(input())
roads = list(map(int,input().split()))
costs = list(map(int,input().split()))

value = 0
m=costs[0]
for i in range(n-1):
    if costs[i] < m : # cost[i]가 더 작다면
        m = costs[i]
    value += m *roads[i]

print(value)