import sys
input= sys.stdin.readline

def init(idx,left,right):
    if left == right:
        tree[idx] = A[left]
        return tree[idx]
    else:
        mid = (left + right) // 2
        l = init(2*idx,left,mid)
        r = init(2*idx+1,mid+1,right)
        tree[idx] = l+r
        return tree[idx]
def getSum(idx,s,e,left,right):
    # 경계밖, 경계안 ,경계사이
    # i) 경계밖일 때
    if left > e or right < s :
        return 0
    # 경계안
    elif s<=left<=right<=e :
        return tree[idx]
    else: #경계사이
        mid = (left+right)//2
        l = getSum(2*idx ,s,e,left,mid)
        r = getSum(2*idx+1,s,e,mid+1,right)
        return l+r

def update(idx,target,diff,left,right):
    # 경계에 속해있다면
    if idx<4*n and left <= target <= right :
        tree[idx] += diff
        mid = (left+right) // 2
        update(2*idx,target,diff,left,mid)
        update(2*idx+1,target,diff,mid+1,right)


n = int(input())
A = list(map(int,input().split()))
m = int(input())
tree = [0 for i in range(4*n)]
A.insert(0,0)
updateQuery = []
originSumQuery = []
answer = {}

for i in range(m):
   query = list(map(int,input().split()))
   if query[0] == 1:
       updateQuery.append(query)
   else:
       originSumQuery.append(query)

sumQuery= sorted(originSumQuery,key=lambda x : x[1])
init(1,1,n)
curUpdateIdx = 0

for prefix,updateIdx,s,e in sumQuery:
    if updateIdx == curUpdateIdx:
        answer[str([prefix,updateIdx,s,e])]= getSum(1,s,e,1,n)

    else: #업뎃이 안됐으니 그만큼 업뎃을 해주고 답지에 기록
        while curUpdateIdx != updateIdx:
            curUpdateIdx += 1
            prefix,idx,value = updateQuery[curUpdateIdx-1]
            diff= value - A[idx]
            update(1,idx,diff,1,n)
            A[idx] = value
        answer[str([2,updateIdx,s,e])] = getSum(1,s,e,1,n)

for prefix,updateIdx,s,e in originSumQuery:
    print(answer[str([prefix,updateIdx,s,e])])

