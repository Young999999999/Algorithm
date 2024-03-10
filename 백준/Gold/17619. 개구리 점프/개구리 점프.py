N,Q = map(int,input().split())

def find(x): # 자신이 속한 집합을 찾는다
    if arr[x] == x :
        return x

    arr[x] = find(arr[x])
    return arr[x]

def merge(a,b):
    a = find(a)
    b = find(b)

    if a != b: # 다른 집합이라면 합집합 연산 수행
        MIN,MAX = min(a,b) , max(a,b)
        arr[MAX] = MIN


def isUnion(a,b):
    a=find(a)
    b=find(b)

    if a==b: # 같은 집합이다. 그러므로 통나무를 건널 수 있다
        return True
    return False


arr=[i for i in range(N+1)]
tree =[[i,0,0,0] for i in range(N+1)]


for i in range(1,N+1):
    a,b,c = map(int,input().split())
    tree[i][1],tree[i][2],tree[i][3] = a,b,c

tree.sort(key = lambda x : x[1]) # 통나무의 시작 지점 순으로 정렬

for i in range(N):
    cnum,cs,ce,cy = tree[i]
    nnum,ns,ne,ny = tree[i+1]

    if ce >= ns : # union 해야함
        merge(cnum,nnum)


for i in range(Q):
    a,b = map(int,input().split())

    if isUnion(a,b):
        print(1)
    else:
        print(0)






