import sys
from collections import deque
input = sys.stdin.readline

row,column = map(int,input().split())
iceburg = [list(map(int,input().split())) for i in range(row)]
vector = [[-1,0],[1,0],[0,-1],[0,1]]

def search(x,y):
    q = deque()
    q.append((x, y))
    visited[y][x] = True

    while q:

        x, y = q.popleft()

        for dx, dy in vector:
            nx = x + dx
            ny = y + dy

            if -1 < nx < column and -1 < ny < row:
                if not visited[ny][nx] and iceburg[ny][nx] != 0:
                    visited[ny][nx] = True
                    q.append((nx,ny))

def countWater(x,y):

    for dx,dy in vector:
        nx = x + dx
        ny = y + dy

        if -1<nx<column and -1<ny<row:
            if iceburg[ny][nx] == 0 : #바다와 인접하다면
                melt[y][x] += 1

def meltIceburg():
    for i in range(row):
        for j in range(column):
            if melt[i][j] != 0 :
                iceburg[i][j] = max(0,iceburg[i][j] - melt[i][j])


def BFS(x,y):
    q=deque()
    q.append((x,y))

    visited[y][x] = True

    while q:

        x,y = q.popleft()
        countWater(x, y)

        for dx, dy in vector:
            nx = x + dx
            ny = y + dy

            if -1 < nx < column and -1 < ny < row:
                if not visited[ny][nx] and iceburg[ny][nx] != 0 :
                    visited[ny][nx] = True
                    q.append((nx,ny))


time = 0
while True:
    cnt = 0
    visited = [[False for i in range(column)] for j in range(row)]
    melt = [[0 for i in range(column)] for j in range(row)]
    x,y= 0,0

    for i in range(row):
        for j in range(column):
            if not visited[i][j] and iceburg[i][j] != 0:
                search(j,i)
                x,y = j,i
                cnt += 1

            if cnt == 2:
                print(time)
                exit(0)

    if cnt == 0:
        print(0)
        exit(0)

    visited = [[False for i in range(column)] for j in range(row)]

    BFS(x,y)
    meltIceburg()
    time += 1







