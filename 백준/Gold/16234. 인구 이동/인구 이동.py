import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
# 국경값 계산후 최신화
# 방문 일수가 며칠인지  O


def DFS(x,y):
    if visited[y][x]:
        return
    visited[y][x] = True

    for i in vector :
        dx,dy = i
        next_x = dx + x
        next_y = dy + y

        if next_x == N or next_x <0 or next_y == N or next_y <0 : #bound limit
            continue

        diff = abs(matrix[y][x] - matrix[next_y][next_x])

        if not visited[next_y][next_x] and diff >=L and diff <=R : #인접 국경의 차이 diff가 L과 R 사이에 위치한다면 국경선을 개방한다

            location.append((next_x,next_y))
            value.append(matrix[next_y][next_x])
            DFS(next_x,next_y)






N,L,R = map(int,input().split())
matrix =[]
vector = [[-1,0],[1,0],[0,1],[0,-1]] # 상 하 좌 우 벡터



for i in range(N):
    matrix.append(list(map(int,input().split())))

cnt = 0
while True:
    bit = 0
    visited=[[False for i in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            location=[(j,i)]
            value = [matrix[i][j]]
            DFS(j,i)

            if len(location) >= 2: #국경을 이었다
                avg=int(sum(value)/len(location))
                bit= 1
               # print(cnt)
               # print("Befo")
               # print(value)
               # print(location)
               # for l in matrix:
               #     print(l)
                for k in location:
                    x,y = k
                    matrix[y][x] = avg
                #print("After")
               # for l in matrix:
                #    print(l)
    if bit == 1:
        cnt+=1
    else:
        print(cnt)
        exit(0)