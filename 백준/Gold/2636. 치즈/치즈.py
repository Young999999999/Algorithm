import sys
from collections import deque
input= sys.stdin.readline

def getCheese():
    cnt = 0
    for i in matrix:
        tmp = i.count(1)
        cnt += tmp

    return cnt

def bfs():

    q= deque()
    q.append((0,0))
    visited = [[False for i in range(w)] for j in range(h)]
    vector =[[-1,0],[1,0],[0,1],[0,-1]]
    visited[0][0] = True

    while q:
        x,y = q.popleft()

        for dx,dy in vector:

            nx = x+dx
            ny = y+dy

            if 0 <= nx < w and 0 <= ny < h: # 바운드 설정

                if not visited[ny][nx] and matrix[ny][nx]!= 1 : #아직 미방문 and 치즈가 아니라면 큐 삽입
                    q.append((nx,ny))
                    visited[ny][nx] = True

                if matrix[ny][nx] == 1 : #치즈라면 녹인다
                    matrix[ny][nx] = 0 #큐에 삽입하지는 않는다.
                    visited[ny][nx] = True


h,w = map(int,input().split())

matrix=[]

for i in range(h):
    matrix.append(list(map(int,input().split())))


prev = 0
cnt = 0
while True:
    cheese = getCheese()
    if cheese == 0 :
        break

    prev = cheese
    bfs()
    cnt += 1

print(cnt)
print(prev)