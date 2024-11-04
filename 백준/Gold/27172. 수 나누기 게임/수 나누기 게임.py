def yaksu(num):
    l = [1]
    for i in range(2,int(num**(1/2))+1):
        if num % i == 0:
            l.append(i)
            l.append(num//i)

    return set(l)


n = int(input())
num = list(map(int,input().split()))
judge = [False] * 1000001
result = [0] * 1000001
for i in num:
    judge[i] = True

for i in num:
    l = yaksu(i)
    for j in l:
        if judge[j]:
            result[j] += 1
            result[i] -= 1

for i in num:
    print(result[i], end=' ')


