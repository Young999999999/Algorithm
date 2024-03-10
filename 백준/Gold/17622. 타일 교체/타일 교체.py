from collections import deque

#  input : 현재 타일, 다음 타일 ,다음 타일의 좌표, 다음 타일을 탐색할 방향, k
# output : 방문할 수 있는 여부
def judge(cur,next,dir):

    if cur == 0 :
        if dir == 'R':
            if next in [1,3,5]:
                return True
        elif dir == 'D':
            if next in [2,4,3]:
                return True

    elif cur == 1 :
        if dir == 'L':
            if next in [0,2,5]:
                return True

        elif dir == 'D':
            if next in [2,4,3]:
                return True

    elif cur == 2:
        if dir == 'U':
            if next in [0,1,4]:
                return True
        elif dir == 'R':
            if next in [3,5,1]:
                return True


    elif cur == 3:
        if dir == 'L':
            if next in [0,2,5]:
                return True
        elif dir == 'U':
            if next in [4,1,0]:
                return True

    elif cur == 4:
        if dir == 'D':
            if next in [2,3,4]:
                return True
        elif dir == 'U':
            if next in [0,1,4]:
                return True

    elif cur == 5:
        if dir == 'L':
            if next in [0,2,5]:
                return True
        elif dir == 'R':
            if next in [1,3,5]:
                return True

    return False

# input : 현재 타일, 방향
# output : 바꾼 타일

def changeTile(cur,dir):
    return TileDict[cur][dir]


def BFS(startX,startY,K):

    q = deque()
    cur = matrix[N-3][N-1]

    visited[1][startY][startX] = True
    visited[0][startY][startX] = True

    vector = [['L',-1,0],['R',1,0],['U',0,-1],['D',0,1]]
    q.append((cur,startX,startY,K))

    while q:
        cur,x,y,k = q.popleft()

        for dir,dx,dy in vector:
            nx = dx + x
            ny = dy + y

            if -1< ny < N-2 and -1<nx<N:
                if not visited[k][ny][nx]:  #방문하지 않았다면

                    if judge(cur,matrix[ny][nx],dir): #타일 교체 없이 이동가능하다면

                        q.append((matrix[ny][nx],nx,ny,k))
                        visited[k][ny][nx] = True
                        cnt[k][ny][nx] = cnt[k][y][x] + 1

                    else:
                        if k == 1:

                            next = changeTile(cur,dir)

                            if not visited[0][ny][nx] :
                                for i in next:
                                    q.append((i,nx,ny,0))
                                    cnt[0][ny][nx] = cnt[1][y][x] + 1
                                    visited[0][ny][nx] = True





N,K = map(int,input().split())
matrix = []
for i in range(N):
    tmp =[5]
    tmp.extend(list(map(int,input().split())))
    tmp.append(5)

    matrix.append(tmp)

N = N+2

cnt = [[[0 for i in  range(N)]for j in range(N)] for k in range(2)]
visited = [[[False for __ in range(N)] for _ in range(N)] for ___ in range(2)]

for i in range(2):
    for j in range(N):
        visited[i][j][0] = True
        visited[i][j][-1] = True


TileDict = {}
TileDict[0] = { 'R' : [1,3,5] , 'D' : [2,3,4],'L' : [],'U':[]}
TileDict[1] = { 'L' : [0,2,5] , 'D' : [2,3,4],'R' : [],'U' : []}
TileDict[2] = { 'R' : [1,3,5] , 'D' : [],'L':[],'U':[0,1,4]}
TileDict[3] = { 'L' : [0,2,5] , 'U' : [0,1,4],'R':[],'D':[]}
TileDict[4] = { 'U' : [0,1,4] , 'D' : [2,3,4],'L' : [],'R' : []}
TileDict[5] = { 'L' : [0,2,5] , 'R' : [1,3,5],'U':[],'D':[]}

INF = 1e9

visited[0][N-3][N-1] = False
visited[1][N-3][N-1] = False
cnt[0][N-3][N-1] = INF
cnt[1][N-3][N-1] = INF
BFS(0,0,K)

result = [cnt[0][N-3][N-1],cnt[1][N-3][N-1]]

cnt = [[[0 for i in  range(N)]for j in range(N)] for k in range(2)]
visited = [[[False for __ in range(N)] for _ in range(N)] for ___ in range(2)]

visited[0][0][0] = False
visited[1][0][0] = False
cnt[0][0][0] = INF
cnt[1][0][0] = INF


BFS(N-1,N-3,K)
result.append(cnt[0][0][0])
result.append(cnt[1][0][0])
answer = min(result) -1
if result[0] == INF and result[1] == INF and result[2] == INF and result[3] == INF:
    print(-1)
elif answer == (N-2) * (N-2) and K==1:
    print(-1)
else:
    print(answer)

