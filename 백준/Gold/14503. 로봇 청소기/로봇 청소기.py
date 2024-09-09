def clean(x,y):
    global cnt
    if not visited[y][x] and matrix[y][x] == 0:
        cnt += 1
        visited[y][x] = True

def searchNotClean(x,y):
    for dx,dy in vector:
        nx = x + dx
        ny = y + dy
        #아직 청소안한 곳
        if 0<=nx<M and 0 <=ny<N:
            if matrix[ny][nx] == 0 and not visited[ny][nx]:
                return True

    return False

def rotate(d):
    d-=1
    if d>=0:
        return d
    return 3

N,M = map(int,input().split())
y,x,d = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
# d -> 0북 1동 2남 3서
vector = [[0,-1],[1,0],[0,1],[-1,0]]
visited=[[False for i in range(M)] for j in range(N)]
cnt = 0

while True:
    clean(x,y)

    if searchNotClean(x,y):
        d=rotate(d)
        dx,dy = vector[d]
        nx,ny=x+dx,y+dy

        if 0<=nx<M and 0<=ny<N:
            if not visited[ny][nx] and matrix[ny][nx] == 0:
                x,y=nx,ny

    else:
        dx,dy= -vector[d][0],-vector[d][1]
        nx, ny = x + dx, y + dy

        if 0 <= nx < M and 0 <= ny < N and matrix[ny][nx]==0:
            x, y = nx, ny
        else:
            print(cnt)
            exit(0)



