import sys
import time
from collections import deque


q= deque()
input =sys.stdin.readline

def BFS():
    q.append((0,0,K,1)) #x,y의 좌표 , K , 낮(1)인지 밤(0)인지
    visited[K][0][0] = 1

    while q:
        x,y,cnt,time = q.popleft()
        check = 0
        next_time = (time+1) % 2

        for i in vector:
            dy,dx= i
            next_x = x+dx
            next_y = y+dy

            if next_x <0 or next_y <0 or next_x >= M or next_y >=N:
                continue

            if next_x == M - 1 and next_y == N - 1:  # 기저 조건
                return visited[cnt][y][x] + 1

            # case1 벽을 그냥 부술 수 있는 조건 1. 낮이여야함. 2. 벽을 만나야함. 3. cnt가 1이상
            # case2 밤인데 담턴에 벽을 부술 수 있으면 1. 밤이여야함 2. 벽을 만나야함 3. cnt가 1 이상 4. c+1 해줌 다시큐에 삽입
            # case3 일반 조건 1. 벽이 아니면 그냥 삽입  c+1 해줌 cnt도 그대로 input
            # 밤이면 낮인 걸로 다시 q에 삽입
            #case3
            if visited[cnt][next_y][next_x] ==0 and matrix[next_y][next_x] == 0 : # 벽이 아니고 미방문
                visited[cnt][next_y][next_x] = visited[cnt][y][x] + 1
                q.append((next_x, next_y, cnt, next_time))

            #case1 벽 부숨
            elif visited[cnt-1][next_y][next_x] == 0 and matrix[next_y][next_x] == 1 and time ==1 and cnt >=1:
                visited[cnt-1][next_y][next_x] = visited[cnt][y][x] + 1
                q.append((next_x,next_y,cnt-1,next_time))

            #case2
            elif visited[cnt][next_y][next_x] == 0 and matrix[next_y][next_x] == 1 and time == 0 and cnt >=1:
                check = 1
                q.append((x,y,cnt,next_time))
        if check == 1:
            visited[cnt][y][x] = visited[cnt][y][x] + 1

    return -1
N,M,K = map(int,input().split())
if N == 1 and M==1 :
    print(1)
    exit(0)

matrix= []
visited= [[[0 for  i in range(M)] for j in range(N)] for k in range(K+1)]

vector = [[-1,0],[1,0],[0,-1],[0,1]] #상하좌우 방향벡터

for i in range(N):
    arr=list(map(int,input().strip()))
    matrix.append(arr)
#
# start = time.time()
print(BFS())
#
# print(f"측정 시간 : {time.time() - start}")
