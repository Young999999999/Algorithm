def man(n):
    idx = n

    while idx <= num:
        changeStatus(idx-1)
        idx += n


def girl(n):
    idx = 1

    while True:
        if switch[n-idx-1:n-1] == switch[n:n+idx][::-1]:
            idx +=1
        else:
            idx -= 1
            break

    for i in range(n-idx,n+idx+1):
        changeStatus(i-1)


def changeStatus(idx):

    if switch[idx] == 0:
        switch[idx] = 1
    else:
        switch[idx] = 0



num = int(input())
switch = list(map(int, input().split()))

k = int(input())

for i in range(k):
    gender, n = map(int,input().split())

    if gender == 1:
        man(n)

    else:
        girl(n)


for i in range(1,num+1):

    print(switch[i-1], end=' ')

    if i%20 == 0:
        print()