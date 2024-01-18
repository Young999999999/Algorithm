n = int(input())

# 1 3 2 0 5 3 3  -> 4
# 3 5 3 3 -> 3
# 2 3 5 10 5 -> 4
# 1 3 2 0 3 5 3 3 -> 5

def judge(idx):
    if idx <= n-3 and matrix[idx+1] == (matrix[idx] + matrix[idx+2]):
        return True

    return False



matrix = list(map(int,input().split()))
diff = [0] * n
cnt = 0

idx = -1
while idx < n-1:
    idx+= 1 # 현재 인덱스
    cur = matrix[idx] - diff[idx]

    next_idx = min(n-1,idx+1) #인덱스 에러 방지
    next = matrix[next_idx]

    if cur == 0 or matrix[idx] == 0:
        continue

    #print("index = ", idx)

    if cur > next : # 하나의 칸에 0을 넣었다고 생각
        cnt += 1

    elif cur == next :
        cnt += 1
        idx += 1

    elif matrix[idx] == next:
        idx += 1
        cnt += 1

    elif judge(idx):
        idx += 2
        cnt += 2

    elif cur < next :
        diff[next_idx] = cur
        cnt += 1




print(cnt)