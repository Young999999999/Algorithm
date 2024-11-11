import sys
input = sys.stdin.readline
g = int(input())
p = int(input())
planes = [int(input()) for _ in range(p)]
visited = [[0] * 101 for _ in range(1001)]
for i in range(1001):
    visited[i][0] = 100

def getIdx(value,bit):
    idx = value // 100

    if idx == 0 and bit:
        return -1,-1

    if bit:
        idx-=1

    for i in range(idx,-1,-1):
        if visited[i][0] :
            if bit:
                return i,100
            else:
                return i,value % 100

    return -1,-1

cnt = 0
for plane in planes:
    idx,cursor = getIdx(plane,0)
    bit = 0
    if idx >= 0:
        for i in range(cursor,0,-1):
            if not visited[idx][i]:
                visited[idx][i] = 1
                visited[idx][0] -= 1
                cnt += 1
                bit = 1
                break

        if not bit:
            idx,cursor = getIdx(plane, 1)
            if idx == -1:
                print(cnt)
                exit(0)

            for i in range(cursor, 0, -1):
                if not visited[idx][i]:
                    visited[idx][i] = 1
                    visited[idx][0] -= 1
                    cnt += 1
                    break

    else: #출력 해야해
        print(cnt)
        exit(0)
print(cnt)