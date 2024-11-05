import sys
input =sys.stdin.readline

n =int(input())
str = []


for i in range(n):
    s=input().strip()
    len_s=len(s)
    str.append([len_s,s])

str.sort( key = lambda x : (x[0],x[1]))
tmp =''
for i in str :
    
    if tmp != i[1]:
        print(i[1])
    tmp =i[1]


