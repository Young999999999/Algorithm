n = int(input())
sequence = list(map(int,input().split()))
sequence.reverse()
INF = int(1e9)
stack = [INF]
answer = [0 for i in range(n)]
for i in range(n):
    now = sequence[i]

    while stack[-1] <= now:
        stack.pop()

    answer[i] = stack[-1]
    stack.append(now)

def convert(x):
    if x == INF:
        return -1
    return x

answer = reversed(list(map(convert,answer)))
print(*answer)

