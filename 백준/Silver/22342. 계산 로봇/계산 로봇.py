n,m = map(int,input().split())

matrix = []
for i in range(n):
    matrix.append(list(map(int,input())))


robot = [[[0,0,0] for i in range(m)] for j in range(n)]


def setStore(x,y):
    global result

    MAX = 0
    for dy in [y-1,y,y+1]:
        if -1<dy<n and -1<x-1:
            MAX = max(MAX,robot[dy][x-1][2])

    result = max(MAX,result)
    robot[y][x][1] = MAX

def setOutput(x,y):
    robot[y][x][2] = robot[y][x][1] + matrix[y][x]


result = 0

for i in range(m):
    for j in range(n):
        setStore(i,j)
        setOutput(i,j)


print(result)


















