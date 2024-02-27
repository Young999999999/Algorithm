import sys
input= sys.stdin.readline

n=int(input())

arr = list(map(int, input().split()))

result=[1]*n
bigarr=[]
for i in range(0,n,1): # 나보다 큰 놈들 다 bigarr에 집어 넣고 가장 작은 거 값 골라서 합쳐주면 되겠찌용 ?
    num=0
   #print(bigarr)
    bigarr=[0]

    for j in range(0,i,1): # 나보다 좌측에 있는 놈들
        if (arr[i]>arr[j]):
              #젤 작은 인덱스값 = num
            num=j
            bigarr.append(result[num])

    result[i]=max(bigarr) + 1

print(max(result))