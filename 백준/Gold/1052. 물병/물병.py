candidate = []
n = 1
for i in range(30):
    candidate.append(n)
    n *= 2
    if n >= 10**7:
        break
candidate.reverse()
n,k = map(int,input().split())

SUM = n
for i in range(k):
    for num in candidate:
        if num < SUM:
            SUM -= num
            break


print(num-SUM)
