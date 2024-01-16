import sys
input = sys.stdin.readline

# 문제 입력
N = int(input())

A=[]
B=[]

for i in range(N):
    A.append(list(map(int,input().split())))

for i in range(N):
    B.append(list(map(int,input().split())))


# 반시계로 회전 구현.
def rotate(A):
    tmp = []
    for i in range(1,N+1):
        tmp.append([i for i in range(i)])

    for i in range(N): # 아래 선분의 기준, 인덱스의 기준
        for j in range(i,N): # 선분의 요소 대입
            tmp[N-i-1][j-i] = A[j][i]

    return tmp

def calculator(A,B):
    cnt = 0

    for i in range(N):
        for j in range(i,N):
            if A[j][i] != B[j][i] :
                cnt+=1

    return cnt

MIN = 1e9

for i in range(3):
    MIN = min(MIN,calculator(A,B))
    A = rotate(A)

#대칭 구현
symmetry = []
for i in range(1,N+1):
    symmetry.append([i for i in range(i)])

for i in range(N):
    for j in range(i+1):
        symmetry[i][i-j] = A[i][j]


for i in range(3):
    MIN = min(MIN,calculator(symmetry,B))
    symmetry = rotate(symmetry)

print(MIN)
