n = int(input())
sequence = list(map(int,input().split()))
X = int(input())
sequence.sort()
answer = 0
for i in range(n):
    std = sequence[i]
    l = 0
    r = n-1
    for j in range(20):
        mid = (l+r)//2
        if std + sequence[mid] >= X :
            r = mid
        else:
            if std + sequence[mid] == X:
                answer += 1
                break

            l = mid

    if std + sequence[r] == X:
        answer += 1

print(answer//2)