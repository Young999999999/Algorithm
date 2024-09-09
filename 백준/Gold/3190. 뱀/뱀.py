from collections import deque

def move(x,y,dir):
    dx,dy = vector[dir]
    nx,ny = x+dx, y+dy
    if 0<=nx<n and 0<=ny<n and (matrix[ny][nx] == 0 or matrix[ny][nx] == 'A') :
        if matrix[ny][nx] == 'A':
            matrix[ny][nx] = matrix[y][x] + 1
        else:
            matrix[ny][nx] = matrix[y][x] + 1
            tail_x, tail_y = snake.popleft()
            matrix[tail_y][tail_x] =0

    else: #벽,자신의 몸에 박아 게임끝

        global cnt
        print(cnt)
        exit(0)
    snake.append((nx,ny))
    return nx,ny
def rotate(dir,v):
    if v == 'L':
        return (dir+3)%4
    if v == 'D':
        return (dir+1)%4

dir = 0
#동 남 서 북
snake=deque()
snake.append((0,0))
vector = [[1,0],[0,1],[-1,0],[0,-1]]
cnt = 0
x,y =0,0
n = int(input())
matrix=[[0 for i in range(n)] for j in range(n)]
k = int(input())
apple = [list(map(int,input().split())) for i in range(k)]
for ay,ax in apple:
    matrix[ay-1][ax-1] = 'A'
l = int(input())
time = [list(input().split()) for i in range(l)]
time.reverse()

while True:
    cnt += 1
    x,y = move(x,y,dir)

    if len(time) >0 :
        t,v = int(time[-1][0]),time[-1][1]

    if t == cnt :
        dir = rotate(dir,v)
        time.pop()





