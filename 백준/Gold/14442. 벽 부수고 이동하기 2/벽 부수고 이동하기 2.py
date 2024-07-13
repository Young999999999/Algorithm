import sys
from collections import deque
q= deque()
input= sys.stdin.readline

def BFS():
    q.append((0,0,K))
    vector = [[-1,0],[1,0],[0,-1],[0,1]]
    visited[K][0][0] = True
    while q:
        x,y,cnt=q.popleft()
        for i in vector:
            dx,dy = i
            next_x = x+dx
            next_y = y+dy

            if next_x <0 or next_x >= M or next_y <0 or next_y >= N: #bound
                continue

            if not visited[cnt][next_y][next_x] :
                if next_y == N-1 and next_x == M-1:
                    print(count[y][x]+2)
                    return False

                if matrix[next_y][next_x] ==1 and cnt>=1: #벽 부시는 case
                    q.append((next_x, next_y, cnt - 1))
                    visited[cnt][next_y][next_x] = True
                    count[next_y][next_x] =count[y][x]+1
                    continue

                if matrix[next_y][next_x] == 0 : # 벽이 아니에유
                    visited[cnt][next_y][next_x] = True
                    count[next_y][next_x] = count[y][x] + 1
                    q.append((next_x,next_y,cnt))

    return True

#입력시작
N,M,K = map(int,input().split())
visited=[[[False for i in range(M)] for i in range(N)]for i in range(K+1) ]
matrix=[]
count=[[0 for i in range(M)]for i in range(N)]

for i in range(N):
    a=list(map(int,input().strip()))
    matrix.append(a)

#입력종료
if N == 1 and M== 1:
    print(1)
    exit(0)
if BFS():
    print(-1)

