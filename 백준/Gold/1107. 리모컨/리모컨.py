# ban이 아닌 것 중에 가장 가까운 수 찾기
def judge(x):
    if x in ban:
        return True
    return False

n = int(input())
k = int(input())
if k == 0:
    print(min(len(str(n)),abs(n-100)))
    exit(0)
ban = list(map(int,input().split()))
MIN = abs(n-100)
targetNum = list(str(n))
for i in range(1000001):
    candidateNum = list(str(i))
    bit = 0
    for j in candidateNum:
        if judge(int(j)):
            bit = 1
            break
    if bit == 1:
        continue
    cnt = abs(i-n)
    MIN = min(MIN,cnt + len(str(i)))

print(MIN)







