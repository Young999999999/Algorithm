from collections import deque

t = int(input())

def bfs():
    q = deque(fire)

    while q:
        x,y,type,cnt = q.popleft()

        for dx,dy in vector:
            nx = x + dx
            ny = y + dy

            if -1<nx<w and -1<ny<h :
                if not visited[ny][nx] and matrix[ny][nx] == '.':
                    q.append((nx,ny,type,cnt+1))
                    visited[ny][nx] = True

            else: #빌딩 밖에 나간경우
                if type == 'm':
                    print(cnt+1)
                    return

    print("IMPOSSIBLE")

for i in range(t):
    w, h = map(int, input().split())
    visited = [[False] * w for i in range(h)]
    vector = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    matrix = [list(input()) for i in range(h)]
    fire = []
    me = []

    for i in range(h):
        for j in range(w):
            if matrix[i][j] == '@':
                me.append((j, i, 'm', 0))
                visited[i][j] = True
            elif matrix[i][j] == '*':
                fire.append((j, i, 'f', 0))
                visited[i][j] = True

    fire.extend(me)
    bfs()







