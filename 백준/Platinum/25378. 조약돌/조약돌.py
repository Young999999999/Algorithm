n = int(input())
stone=list(map(int,input().split()))
stone.insert(0,0)
cnt = n
prefix = []
sub = 0
INF = 1e9

def subtract(x):
    global sub
    if sub - x < 0 or x == INF :
        return INF

    return sub-x

for i in range(1,n+1):

    if stone[i] in prefix:
        prefix = []
        cnt -= 1
        continue

    sub = stone[i]
    prefix = list(map(subtract,prefix))
    prefix.append(stone[i])

result = [0,0]
result[0] = cnt

for i in range(n,0):

    if stone[i] in prefix:
        prefix = []
        cnt -= 1
        continue

    sub = stone[i]
    prefix = list(map(subtract,prefix))
    prefix.append(stone[i])

result[1] = cnt

print(min(result))













