import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

def find(node):
    if union_arr[node]==-1:
        return node
    else:
        union_arr[node]=find(union_arr[node])
        return union_arr[node]

def merge(a,b):
    a=find(a)
    b=find(b)

    if a==b: # is_union 이미 a,b 같은 집합에 소속되어있다
        return

    # 노드를 잇는 과정
    big_node=max(a,b)
    small_node=min(a,b)
    union_arr[big_node]=small_node

def is_union(a,b):
    a=find(a)
    b=find(b)

    if a==b:
        print("YES")
    else:
        print("NO")


n,m = map(int,input().split())
union_arr=[-1]*(n+1)

for i in range(m):
    op,a,b=map(int,input().split())
    if op == 0:
        merge(a,b)
    else:
        is_union(a,b)


