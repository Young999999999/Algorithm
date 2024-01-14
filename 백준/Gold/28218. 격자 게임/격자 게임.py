from collections import deque

import sys
input= sys.stdin.readline

def BFS(start_y,start_x):
    q=deque()
    q.append((start_y,start_x,0))

    while q:
        now_y,now_x,cnt = q.popleft()

        for i in vector:
            dy,dx = i

            next_y = dy + now_y
            next_x = dx + now_x

            if 0 <= next_y < N and 0 <= next_x < M:
                if not visited[next_y][next_x] and not matrix[next_y][next_x] == '#':
                    visited[next_y][next_x] = True
                    q.append((next_y,next_x,cnt+1))

                    if next_y == N-1 and next_x == M-1:
                        return cnt+1


N,M,K = map(int,input().split())

#vector 설정
vector = [[i,i] for i in range(1,K+1)]
vector.append([1,0])
vector.append([0,1])


matrix = []

for i in range(N):
    matrix.append(list(input().strip()))

Q = int(input())

for i in range(Q):
    start_y,start_x = map(int,input().split())
    visited = [[False for i in range(M)] for j in range(N)]
    num = BFS(start_y-1,start_x-1)

    if num % 2 == 0:
        print('Second')
    else:
        print('First')


