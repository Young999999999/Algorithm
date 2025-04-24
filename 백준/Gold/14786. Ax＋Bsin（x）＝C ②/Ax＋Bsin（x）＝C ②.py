import math
import sys
input = sys.stdin.readline

A,B,C = map(int,input().split())

def f2(x):
    return B * math.sin(x)

def f1(x):
    return -A*x + C

def Binary_Search(x):
    s= i-1
    e= i

    for j in range(1000000):
        mid = (s+e)/2
        if f1(mid) <= f2(mid):
            e= mid-0.00000000001
        else:
            s=mid+0.00000000001

    return mid



# -ax+C와 bsinx 가 만나는 지점의 x 좌표를 구하면 된다
# -ax+C <= bsinx 가 정수 기준으로 더 작아진다면?
# x는 i-1~i에 위치하게 되는 것이다

# 범위를 줄이고 이분 탐색으로 더 탐색해보자

for i in range(0,100001):
    if f1(i) <= f2(i):
        break



print(Binary_Search(i))

