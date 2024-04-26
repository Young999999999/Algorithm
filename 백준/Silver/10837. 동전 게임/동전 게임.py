import sys
input = sys.stdin.readline


k = int(input())
d = 0

iter = int(input())
for i in range(iter):
    a,b = map(int,input().split())
    bit = 0

    if a==b:
        print(1)
    elif b>a and b-a <= k-b+1:
        print(1)

    elif a>b and a-b<= k-a+2:
       print(1)
    else:
        print(0)


