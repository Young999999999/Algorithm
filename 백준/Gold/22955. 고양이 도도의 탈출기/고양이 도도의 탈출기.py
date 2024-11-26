import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(input()) for i in range(n)]
xVector = [-1,1]
yVector = [0,1]
pos = [0, 0]
d = [[0]* m for i in range(n)]

flag = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 'C':
            pos = [j, i]
            flag = 1
            break

    if flag:
        break

def fall():
    for x in range(m):
        preY = n - 1
        for y in range(n-2,-1,-1):
            if matrix[y][x] == 'X':
                d[y][x] = preY
            else:
                preY = y

fall()

def bfs(x, y):
    q = []
    heapq.heappush(q, (0, x, y))

    while q:
        cnt, x, y = heapq.heappop(q)
        if matrix[y][x] == 'E':
            print(cnt)
            exit(0)

        elif matrix[y][x] == 'X':
            ny = d[y][x]

            if not matrix[ny][x] == 'D':
                heapq.heappush(q, (cnt + 10, x, ny))
            continue
        
        elif matrix[y][x] == 'D':
            continue

        for dx in xVector:
            nx = x + dx

            if 0 <= nx <= m - 1:
                if not matrix[y][nx] == 'D':
                    heapq.heappush(q, (cnt + 1, nx, y))

        for dy in yVector:
            ny = y + dy

            if  1 <= ny <= n - 1:
                if matrix[ny][x] == 'L' and dy == 0 and not matrix[y - 1][x] == 'D':
                    heapq.heappush(q, (cnt + 5, x, y - 1))
                elif matrix[ny][x] == 'L' and dy == 1 and not matrix[y + 1][x] == 'D':
                    heapq.heappush(q, (cnt + 5, x, y + 1))

        matrix[y][x] = 'D'


x, y = pos
bfs(x, y)
print("dodo sad")

# 2 3
# CLF
# EFL

