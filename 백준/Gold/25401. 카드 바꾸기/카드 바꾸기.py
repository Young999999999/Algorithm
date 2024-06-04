n = int(input())
diff = [[] for i in range(n)]
num = list(map(int,input().split()))

# 성능 개선, diff의 두번째 for start = i 로 수정
# diff -> (인덱스,i+1과의 차이)
for i in range(n):
    for j in range(i+1,n):
        diff[i].append((num[j] - num[i])//(j-i))

MAX = 0

for i in range(n): # p1
    for d in diff[i]: # p2
        cnt = 0
        for j in range(n):

            if  num[j] == num[i] +(j-i) * d :
                cnt += 1

        MAX = max(MAX,cnt)

print(n-MAX)
