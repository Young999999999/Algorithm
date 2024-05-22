import sys
input = sys.stdin.readline

def update(idx,left,right,value,size):

    if left == right == value :
        tree[idx] += size
        return

    if left <= value <= right :

        tree[idx] += size
        mid = (left+right) // 2
        update(2*idx,left,mid,value,size)
        update(2*idx+1,mid+1,right,value,size)

def getOrder(idx,left,right,order):
    tree[idx] -= 1
    if left == right :
        print(left)
        return

    l = tree[2*idx]
    mid = (left+right) // 2

    if l < order: # 우측 이동
        getOrder(2*idx+1,mid+1,right,order-l)
    else:
        getOrder(2*idx,left,mid,order)

end = 1000000
tree = [0] * end * 4

n = int(input())

for i in range(n):
    query = list(map(int,input().split()))

    if query[0] == 1:
        getOrder(1,1,end,query[1])
    else:
        update(1,1,end,query[1],query[2])


