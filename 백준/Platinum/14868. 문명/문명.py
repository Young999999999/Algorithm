import sys
import time
from collections import deque
input = sys.stdin.readline

def find(a) :
    x= a[0]
    y= a[1]

    if arr[y][x] == [-1,-1] :
        return [x,y]

    arr[y][x] = find(arr[y][x])

    return arr[y][x]

def merge(a,b):
    a = find(a)
    b = find(b)

    if a == b:
        return

    tmp = [min(a,b),max(a,b)]

    arr[tmp[0][1]][tmp[0][0]][0] = tmp[1][0]
    arr[tmp[0][1]][tmp[0][0]][1] = tmp[1][1]

def isUnion(start):

    dict = {}
    for i in range(len(start)):
        parent = find(start[i])

        dict[str(parent)] = 1

    if len(dict) == 1:
        return True
    return False



def BFS(start):
    global CNT
    q = deque(start)

    for x,y in start:
        visited[y][x] = True

    vector = [[-1,0],[1,0],[0,1],[0,-1]]


    while q:
        x,y =q.popleft()

        for dx,dy in vector:
            nx = x + dx
            ny = y + dy

            if 1 <= nx <= N and 1 <= ny <= N :
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    cnt[ny][nx] = cnt[y][x] + 1
                    q.append((nx,ny))
                    merge([x,y],[nx,ny])

                    for dx2,dy2 in vector:

                        nnx = nx + dx2
                        nny = ny + dy2

                        if 1 <= nnx <= N and 1 <= nny <= N:
                            if visited[nny][nnx]  and find([nnx,nny]) != find([nx,ny]):

                                merge([nx,ny],[nnx,nny])
                                CNT -= 1

                                if CNT == 0:
                                    print(max(list(map(max, cnt))))
                                    return


N,K = map(int,input().split())

cnt= [[0 for i in range(N+1)] for j in range(N+1)]
arr = [[ [-1,-1] for i in range(N+1)] for j in range(N+1)]
visited = [[False for i in range(N+1)] for j in range(N+1)]
start = []
CNT = K-1
for i in range(K):
    x,y=map(int, input().split())

    start.append([x,y])
    visited[y][x] = True


vector2= [[-1,0],[1,0],[0,1],[0,-1]]
parent = list(map(find,start))

init_q =deque(start)
while init_q:
    nx,ny =init_q.popleft()

    for dx2, dy2 in vector2:

        nnx = nx + dx2
        nny = ny + dy2

        if 1 <= nnx <= N and 1 <= nny <= N:
            if visited[nny][nnx] :
                merge([nx, ny], [nnx, nny])


dict = {}
for i in start:
    dict[str(find(i))] = 1

set_cnt = len(list(dict.keys()))
CNT = set_cnt -1


if isUnion(start):
    print(0)
    exit(0)

BFS(start)