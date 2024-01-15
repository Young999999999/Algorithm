import sys
input= sys.stdin.readline

def judge(x):

    if not visited[x-1]  and  not visited[(x+1)%n] :
        visited[x] = True






n = int(input())
c =list(map(int,input().split()))
visited=[False]*(n)

result = sum(c)

locate =0
for i in range(n):
    if c[i] > 0 :
        locate = i
        break



if result == 0: #쪽방이 없는 경우 어느 부분을 start로 잡든 상관이 없음
    for i in range(n):
        if c[i] == 0 :
            judge(i)

else: # 쪽방이 있는경우 쪽방 옆의 방을 무조건 선택해야함.
    for i in range(locate+1,locate+1+n):
        cur = i % n

        if c[cur] == 0:
            judge(cur)

SUM = visited.count(True)
print(result+SUM)
