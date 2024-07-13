import sys
input = sys.stdin.readline

def find(x):
    if arr[x] < 0:
        return x
    else:
        arr[x] = find(arr[x])
        return arr[x]

def merge(x,y):
    x = find(x)
    y = find(y)
    if x==y:
        return abs(arr[x])
    a=max(x,y)
    b=min(x,y)
    sum=arr[a]+arr[b]

    arr[b]=sum
    arr[a]=b
    return abs(arr[b])

def isUnion(x,y):
    x = find(x)
    y = find(y)
    if(x==y):
        return 1
    else:
        return 0

n=int(input())



for i in range(n):
    m=int(input())
    i=1
    arr = [-1] * (200001)
    dic={}
    for j in range(m):
        name1,name2 = input().split()
        TF1=name1 in dic
        TF2=name2 in dic
        if TF1 == False:  #이름이 dictionary에 없다면 이름과 해시값을 추가
            dic[name1] = i
            i+=1
        if TF2 == False:
            dic[name2] = i
            i+=1
        print(merge(dic[name1],dic[name2]))