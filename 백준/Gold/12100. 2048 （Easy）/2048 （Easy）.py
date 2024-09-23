MAX = [0]

#judge가 true면 진짜 위로가기
def up(matrix,cnt,judge):
    m =  max([max(i[:]) for i in matrix])
    MAX[0] = max(MAX[0],m)

    if cnt ==5:
        return
    tmp = [[0] * n for i in range(n)]

    for i in range(n):
        values =[]
        for j in range(n):
            if matrix[j][i]:
                values.append(matrix[j][i])

        for j in range(len(values)-1):
            if values[j] == values[j+1]:
                values[j],values[j+1] = 2*values[j],0
        p=0
        for value in values:
            if value:
                tmp[p][i] = value
                p+=1

    if judge:
        up(tmp,cnt+1,True)
        down(tmp,cnt+1)
        left(tmp,cnt+1)
        right(tmp,cnt+1)

    else:
        return tmp

def down(matrix,cnt):
    m = max([max(i[:]) for i in matrix])
    MAX[0] = max(MAX[0], m)

    if cnt ==5 :
        return

    for i in range(n):
        for j in range(n//2):
            matrix[j][i], matrix[n-j-1][i] = matrix[n-j-1][i], matrix[j][i]

    matrix = up(matrix,cnt,False)

    for i in range(n):
        for j in range(n//2):
            matrix[j][i], matrix[n-j-1][i] = matrix[n-j-1][i], matrix[j][i]

    up(matrix,cnt+1,True)
    down(matrix,cnt+1)
    left(matrix,cnt+1)
    right(matrix,cnt+1)


def right(matrix,cnt):
    m = max([max(i[:]) for i in matrix])
    MAX[0] = max(MAX[0], m)

    if cnt == 5:
        return

    tmp = [[0]*n for i in range(n)]

    for i in range(n-1,-1,-1):
        for j in range(n):
            tmp[-i+n-1][j] = matrix[j][i]


    matrix = up(tmp,cnt,False)
    tmp = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            tmp[j][n-i-1] = matrix[i][j]

    up(tmp,cnt+1,True)
    down(tmp,cnt+1)
    left(tmp,cnt+1)
    right(tmp,cnt+1)


def left(matrix,cnt):
    m = max([max(i[:]) for i in matrix])
    MAX[0] = max(MAX[0], m)

    if cnt == 5:
        return

    tmp = [[0] * n for i in range(n)]

    for i in range(n):
        for j in range(n):
            tmp[j][n - i - 1] = matrix[i][j]

    matrix = up(tmp,cnt,False)

    tmp = [[0] * n for i in range(n)]

    for i in range(n):
        for j in range(n):
            tmp[n-j-1][i]= matrix[i][j]

    up(tmp,cnt+1,True)
    down(tmp,cnt+1)
    left(tmp,cnt+1)
    right(tmp,cnt+1)


n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]

up(matrix,0,True)
down(matrix,0)
left(matrix,0)
right(matrix,0)

print(MAX[0])