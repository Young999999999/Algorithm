import sys
input= sys.stdin.readline

def spread():
    vector = [[-1,0],[1,0],[0,-1],[0,1]]
    tmp = [i[:] for i in matrix]

    for y in range(R):
        for x in range(C):
            if matrix[y][x] > 0 :

                quantity = int(matrix[y][x]/5)

                for dx,dy in vector :
                    nx = x + dx
                    ny = y + dy

                    # 1,2 조건
                    if 0<=nx<C and 0<=ny<R and not matrix[ny][nx] == -1:
                        tmp[ny][nx] += quantity
                        tmp[y][x] -= quantity

    return tmp

def excuteAirCleaner():
    tmp = [[0 for i in range(C)] for j in range(R)]
    visited=[[False for i in range(C)] for j in range(R)]
    locate1 = cleaner[0]
    locate2 = cleaner[1]

    # i 우로 다같이 갓
    for i in range(1,C-1):
        tmp[locate1][i+1] = matrix[locate1][i]
        tmp[locate2][i+1] = matrix[locate2][i]
        visited[locate1][i]= True
        visited[locate2][i] = True

    # ii 위로
    for i in range(locate1,0,-1):
        tmp[i-1][C-1] = matrix[i][C-1]
        visited[i][C-1] = True

    # iii 아래로
    for i in range(locate2,R-1):
        tmp[i+1][C-1] = matrix[i][C-1]
        visited[i][C-1] = True

    # 좌로 다같이 갓
    for i in range(C-1,0,-1):
        tmp[0][i-1] = matrix[0][i]
        tmp[-1][i-1] = matrix[-1][i]
        visited[0][i] = True
        visited[-1][i] = True

    # 윗구역이 아래로 슝
    for i in range(locate1):
        tmp[i+1][0]=matrix[i][0]
        visited[i][0] = True

    for i in range(R-1,locate2,-1):
        tmp[i-1][0] = matrix[i][0]
        visited[i][0] = True

    tmp[locate1][0] = -1
    tmp[locate2][0] = -1

    for i in range(R):
        for j in range(C):
            if not visited[i][j]:
                tmp[i][j] = matrix[i][j]
    return tmp



R,C,T = map(int,input().split())
matrix = [list(map(int,input().split())) for j in range(R)]


cleaner=[]

for i in range(R):
    if matrix[i][0] == -1:
        cleaner.append(i)

for i in range(T):
    matrix = spread()
    matrix = excuteAirCleaner()

result = 0
for i in matrix:
    result += sum(i)

print(result+2)