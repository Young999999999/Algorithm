import sys
from collections import deque

input= sys.stdin.readline

def bfs(x,y):
    q =deque()
    t = [(1000,0,0)]
    visited = [[False for i in range(N)] for j in range(N)]
    visited[y][x] = True
    q.append((0,x,y))

    while q:
        time,x,y =q.popleft()

        for i in vector:

            dx = x + i[0]
            dy = y + i[1]

            if -1<dx<N and -1<dy<N  and not visited[dy][dx]:
                if matrix[dy][dx] > shark :
                    visited[dy][dx] = True
                    continue

                elif matrix[dy][dx] < shark and matrix[dy][dx] !=0  : #와쿠 와쿠
                    t.append((time+1,dx,dy))
                    visited[dy][dx] = True
                    q.append((time+1,dx,dy))

                else  : #지나가는길
                    q.append((time+1,dx,dy))
                    visited[dy][dx] = True

    return t #더 이상 먹을 수 있는 물고기가 없다.




N = int(input())

vector = [[-1,0],[1,0],[0,1],[0,-1]]
matrix= []
time = []

shark=2
cnt = 0
for i in range(N):
    matrix.append(list(map(int,input().split())))

start=[]

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 9:
            start.append((j,i))
            matrix[i][j] = 0

result = 0

while True:
    x,y=start.pop()
    time=bfs(x,y)
    time.sort(key=lambda x: (x[0],x[2],x[1]))

    t,rx,ry=time[0][0],time[0][1],time[0][2]
    matrix[ry][rx] = 0
    start.append((rx,ry))

    if t == 1000: #와쿠 와쿠 치가이마스
        break

    result += t
    cnt+=1
    if shark == cnt :
        shark+=1
        cnt = 0


print(result)


