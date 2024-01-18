n=input()
arr = list(map(int,input().split()))

def IsEven(num):

    if num % 2 == 0 :
        return True
    return False

cntOdd = 0
cntEven= 0

for i in arr:
    if IsEven(i):
        cntEven += 1
    else:
        cntOdd += 1

# i ) 홀 + 짝
# ii) 짝 + 홀
cost_i = 0
curCnt = 0
# i)의 경우
for i in range(len(arr)):
    num = arr[i]

    if IsEven(num) == False: #홀수라면
        cost_i += i-curCnt
        curCnt += 1

    if curCnt == cntOdd :
        break

cost_ii = 0
curCnt=0

for i in range(len(arr)):
    num = arr[i]

    if IsEven(num):  # 홀수라면
        cost_ii += i - curCnt
        curCnt += 1

    if curCnt == cntEven:
        break

print(min(cost_i,cost_ii))

