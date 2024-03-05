import sys
input = sys.stdin.readline

n,m = map(int,input().split())


matrix = []
for i in range(n):
    matrix.append(list(map(int,input().strip())))

output =[[0 for i in range(m+1)] for j in range(n+2)]
result = 0



for x in range(1,m+1):
    for y in range(1,n+1):
        MAX = max(output[y - 1][x - 1], output[y][x - 1], output[y + 1][x - 1])

        if result < MAX :
            result = MAX

        output[y][x] = MAX + matrix[y-1][x-1]

print(result)


















