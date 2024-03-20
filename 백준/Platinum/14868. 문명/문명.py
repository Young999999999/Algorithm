import sys
from collections import deque
input= sys.stdin.readline
q=deque()
#Union-Find
def is_union():
    target_x,target_y=init[0]
    tmp = find(N * target_y + target_x)
    for i in init:
        target_x,target_y = i
        a = find(N * target_y + target_x)
        if tmp != a:
            return False
    return True

def find(x):
    if x == arr[x]:
        return x

    arr[x]=find(arr[x])
    return arr[x]

def merge(a,b): #원소 a,b를 합집합하기
    a=find(a)
    b=find(b)

    if a==b: #두 원소가 이미 같은 집합내에 있다. 머지 실패
        return False

    if a>b :
        a,b=b,a
    arr[b]=a

def BFS():

    while q:
        y,x = q.popleft()
        for i in vector:
            dy,dx = i
            next_y = y+dy
            next_x = x+dx

            if next_y <0 or next_y == N or next_x <0 or next_x == N : #matrix bound 초과
                continue

            next_idx = next_y * N + next_x
            cur_idx = y*N + x
            merge(cur_idx, next_idx)

            if is_union():
                print(max(matrix[y][x],matrix[next_y][next_x]))
                return

            if not visited[next_idx]:
                q.append((next_y,next_x))
                matrix[next_y][next_x]=matrix[y][x] + 1
                visited[next_idx] = True




N,K = map(int,input().split())

matrix=[[0 for _ in range(N)] for __ in range(N)]
visited=[False] * (N*N)
arr = [i for i in range(N*N)]
vector = [[-1,0],[1,0],[0,-1],[0,1]]
init =[]




for i in range(K):
    init_x,init_y = map(int,input().split())

    init_x=init_x-1
    init_y=(N+1-init_y)-1
    init.append((init_x,init_y))
    q.append((init_y,init_x)) #이거 방문처리 해줘야함
    visited[init_y*N+init_x] = True
    arr[init_y * N +init_x] =init_y *N + init_x


BFS()





