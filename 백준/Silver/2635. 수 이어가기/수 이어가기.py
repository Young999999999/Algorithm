N = int(input())

result = []

for i in range(1,N+1):
    a = [N, i]
    while True:
        if a[-2] - a[-1] >= 0:
            a.append(a[-2]-a[-1])
        else:
            break

    if len(a) > len(result):
        result = a

print(len(result))
print(*result)