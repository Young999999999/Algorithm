import sys

input = sys.stdin.readline

String = input().strip()
q=int(input())

a = "abcdefghijklmnopqrstuvwxyz"

dict= {}
for i in range(26):
    dict[a[i]] = i

alphabet =[[0 for i in range(26)] for i in range(len(String))]

for i in range(len(String)):
    alphabet[i] = alphabet[i-1][:]
    char=String[i]
    hashcode = dict[char]
    alphabet[i][hashcode] += 1

for _ in range(q):
    l = input().strip().split()
    query, i, j = l[0],int(l[1]),int(l[2])
    cnt =0
    if String[i] == query:
        cnt = 1
    print(alphabet[j][dict[query]] - alphabet[i][dict[query]] + cnt)

# 반복문으로 늘려가자
# alphabet[i+1] = alphabet[i][:]
# char=String[i]
# hashcode = dict[char]
# alphabet[i+1][hashcode] += 1

#query 대응
# q i j
#alphabet[j][dict[q]] - alphabet[i][dict[q]]

