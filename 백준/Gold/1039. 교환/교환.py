def switch(idx,cnt,num):
    if cnt == k:
        global MAX
        MAX = max(MAX,int("".join(num)))
        return

    if idx == len(num)-1:
        if judge():
            switch(idx,cnt+1,num)
            return

        num[-1],num[-2]=num[-2],num[-1]
        switch(idx,cnt+1,num)
        num[-1],num[-2]=num[-2],num[-1]
        return

    if target[idx] == num[idx]:
        switch(idx+1,cnt,num)
        return

    m = max(list(map(int,num[idx+1:])))

    for i in range(idx+1,len(num)):
        if int(num[i]) == m :
            num[i],num[idx] = num[idx],num[i]
            switch(idx+1,cnt+1,num)
            num[i], num[idx] = num[idx], num[i]

def judge():
    for i in cnt:
        if i>=2:
            return True

    return False


num,k = map(int,input().split())
num = list(str(num))

cnt=[0]*10
for i in num:
    cnt[int(i)] += 1

if len(num) == 1:
    print(-1)
    exit(0)
if len(num) == 2:
    if num.count('0'):
        print(-1)
        exit(0)

target = sorted(num,reverse = True)

MAX = -1
switch(0,0,num)
if MAX == -1:
    print(-1)
else:
    print(MAX)

