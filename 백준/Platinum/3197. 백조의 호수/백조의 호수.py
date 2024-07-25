import sys
from collections import deque
q=deque()
input =sys.stdin.readline

def find(x): #집합의 root 찾기
    if x == arr[x] :
        return x
    arr[x]=find(arr[x])
    return arr[x]

def merge(a,b):
    a=find(a)
    b=find(b)
    if a==b: #이미 중복
        return True
    if a > b:
        a,b = b,a
    arr[b] = a

def Baekjo_BFS(y,x):
    p=deque()
    visited=[False]*(R*C+1)

    p.append((y,x))
    while p:
        b,a=p.popleft()
        for i in vector:
            db,da=i
            if b+db < 0 or b+db == R or a+da == C or a+da <0:
                continue
            cur_idx = C * b + a
            next_idx = C*(b+db) + a+da
            visited[cur_idx] = True

            if visited[next_idx] == True:
                continue

            if matrix[b+db][a+da] =='.' or matrix[b+db][a+da] == 'L' : #이미 물이면 합집합 해주자
                merge(cur_idx,next_idx) #물이나 백조만나면 merge
                visited[next_idx] = True
                p.append((b+db,a+da))

def BFS():
    while q:
        y,x =q.popleft()
        for i in vector :
            dy,dx=i
            if y+dy == R or x+ dx == C or  x+ dx <0 or y+dy < 0: #bound 초과
                continue

            cur_idx =  C*y + x
            next_idx = C*(dy+y)+x+dx
            if matrix[y+dy][x+dx] =='.' or matrix[y+dy][x+dx] == 'L' : #이미 물이면 합집합 해주자
                merge(cur_idx,next_idx) #물이나 백조만나면 merge
                if find(L1_idx) == find(L2_idx) :
                    print(max(cnt[y][x],cnt[y+dy][x+dx]))
                    exit(0)
                continue

            if  matrix[y+dy][x+dx] == 'X': #물이 아니라 빙판이라면 하루 지난 날짜 추가
                cnt[y+dy][x+dx] = cnt[y][x] +1
                matrix[y+dy][x+dx]='.'
                q.append((y+dy,x+dx))
                merge(cur_idx,next_idx)

R,C = map(int,input().split())
arr=[i for i in range(C*R+1)]

matrix = [] #빙판과 물의 정보를 담을 matrix
tmp = [matrix.append(list(input().strip())) for i in range(R)]
vector =[[-1,0],[1,0],[0,1],[0,-1]] #상하좌우
cnt =[[0 for i in range(C)] for _ in range(R)] #며칠이 지났는지 알 수 있는 matrix

location = []
for i in range(R): #사전정보 구하기
    for j in range(C):
        if matrix[i][j] =='.' or matrix[i][j] == 'L': #물이라면 q에삽입
            q.append((i,j))
        if matrix[i][j] == 'L':
            location.append([i,j])


loc_y,loc_x=location[0]
L1_idx = C*loc_y + loc_x
loc_y,loc_x=location[1]
L2_idx = C*loc_y + loc_x

Baekjo_BFS(location[0][0],location[0][1]) #미리 백조를 포함하는 애들을 merge해주자
Baekjo_BFS(location[1][0],location[1][1])

BFS()