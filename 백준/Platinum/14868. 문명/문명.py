import sys
from collections import deque
input = sys.stdin.readline

def find(x) :

    if arr[x] == -1 :
        return x

    arr[x] = find(arr[x])

    return arr[x]

def merge(a,b):
    a = find(a)
    b = find(b)

    if a == b:
        return

    if a>b:
        big = a
        small = b
    else:
        big = b
        small = a

    arr[big] = small



def BFS(start):
    global CNT
    q = deque(start)

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
                    curIDX = y*N+x
                    nextIDX =ny*N + nx

                    merge(curIDX,nextIDX)

                    for dx2,dy2 in vector:

                        nnx = nx + dx2
                        nny = ny + dy2

                        nnIDX =nny*N +nnx

                        if 1 <= nnx <= N and 1 <= nny <= N:
                            if visited[nny][nnx]  and find(nnIDX) != find(nextIDX):

                                merge(nextIDX,nnIDX)
                                CNT -= 1

                                if CNT == 0:
                                    print(cnt[ny][nx])
                                    return


N,K = map(int,input().split())

cnt= [[0 for i in range(N+1)] for j in range(N+1)]
arr = [-1] * ((N+1)*(N+1))
visited = [[False for i in range(N+1)] for j in range(N+1)]
start = [[0,0] for i in range(K)]
CNT = K-1
for i in range(K):
    x,y=map(int, input().split())
    start[i][0] = x
    start[i][1] = y
    visited[y][x] = True


vector2= [[-1,0],[1,0],[0,1],[0,-1]]

init_q =deque(start)
while init_q:
    nx,ny =init_q.popleft()
    curIDX = ny * N + nx
    for dx2, dy2 in vector2:

        nnx = nx + dx2
        nny = ny + dy2

        nnIDX = nny*N + nnx
        if 1 <= nnx <= N and 1 <= nny <= N:
            if visited[nny][nnx] :
                merge(curIDX, nnIDX)


dict = {}
for i in start:
    idx = i[1]*N + i[0]
    dict[str(find(idx))] = 1

set_cnt = len(dict)
CNT = set_cnt -1

if CNT == 0:
    print(0)
    exit(0)

BFS(start)