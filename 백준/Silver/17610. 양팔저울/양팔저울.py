import sys
input = sys.stdin.readline


#idx+1 => start idx   cnt => end count   cur => cur count
def BruteForce(idx,cur,result):
    #print(idx, cur, result)

    if cur == k+1 : #이번 회차에서 끝내야함
        return

    else:
        for i in range(idx,k):

            weight[result+chu[i]] = 1
            BruteForce(i+1,cur+1,result+chu[i])


k = int(input())
chu = list(map(int,input().split()))
chu.sort()
sigma = sum(chu)

weight  = [0 for i in range(sigma+1)]

BruteForce(0,0,0)
cnt = 0

for j in chu:
    for i in range(1,sigma+1):
        if weight[i] == 1 and i-j >0:
            weight[i-j] = 1

for i in range(1,sigma+1):
    if weight[i] == 0:
        cnt+=1

print(cnt)
#11061