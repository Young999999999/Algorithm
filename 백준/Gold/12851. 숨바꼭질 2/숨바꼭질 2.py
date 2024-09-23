n,k = map(int,input().split())
visited=[{} for i in range(100001)]
ban = [False] * 100001

if n==k:
    print(0)
    print(1)
    exit(0)

visited[0][n] = 1

for time in range(100000):
    for pos in visited[time]:
        ban[pos] = True
        for next in [pos-1,pos+1,pos*2]:
            if 0<=next<= 100000:
                if next in visited[time+1] and not ban[next]:
                    visited[time+1][next] += visited[time][pos]
                if not next in visited[time+1] and not ban[next]:
                    visited[time+1][next] = visited[time][pos]

    if k in visited[time+1]:
        print(time+1)
        print(visited[time+1][k])
        exit(0)
