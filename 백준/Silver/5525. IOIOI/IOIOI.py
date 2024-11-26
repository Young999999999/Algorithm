import sys
input =sys.stdin.readline

def judge(offset):
    bit = 0
    str = 0

    for i in range(offset,M):
        if bit == 0 and S[i] == 'I':
            bit = 1
            str += 1
            continue

        if bit == 1 and S[i] == 'O':
            str += 1
            bit = 0
            continue
        break

    return str
N = int(input())
M = int(input())
S = input().strip()

offset = 0
result = 0
while True:

    if offset >= M:
        break

    if S[offset] == 'I':

        p = judge(offset)
        offset += p
        #print(p)
        num = (p-1)//2
        if num - N >= 0:
            result += num-N+1

        continue

    offset +=1
print(result)