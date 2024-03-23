import sys
input =sys.stdin.readline

def update(s,e,value): #log(n) 시간의 쿼리 처리
    while s<=e:
        tree[s] += value
        s+=s&-s


def prefix(node): #총 쿼리의 데이터 변동량 구하기
    tmp=0
    while node >=1:
        tmp+=tree[node]
        node -= node & - node

    return tmp

N=int(input())
tree= [0] * (N+1)
arr=list(map(int,input().split()))
M=int(input())
for i in range(M):
    query = list(map(int,input().split()))
    if query[0]==1: # 값 더하기 쿼리
        b,c,d=query[1],query[2],query[3]
        update(b,N,d)
        update(c+1,N,-d)
    elif query[0]==2:
        change = prefix(query[1])
        print(arr[query[1]-1]+change)