
jobs = [list(map(int,input().split())) for i in range(int(input()))]
jobs.sort(key=lambda x:x[1])

def judge(start, jobs):
    now = start
    for t, dueTo in jobs:
        endTime = now + t

        if endTime > dueTo:
            return False

        now = endTime

    return True

result = -1
for i in range(1000001):
    if judge(i, jobs):
        result = i


print(result)

