from collections import deque
n,k = map(int,input().split())
q= deque([n])
cnt=[0] *200001
visited=[False] * 200001
vector = [-1,1]
def bfs():

    while q:
        now = q.popleft()

        # 순간이동처리
        for i in range(20):
            nx = now * (2**i)
            if nx < 150000 and not visited[nx] :
                cnt[nx] = cnt[now]
                visited[nx] = True
                q.append(nx)


        for dx in vector:
            nx = dx + now
            if  0<=nx<200000 and not visited[nx] :
                cnt[nx] = cnt[now] + 1
                visited[nx] = True
                q.append(nx)

bfs()
print(cnt[k])






