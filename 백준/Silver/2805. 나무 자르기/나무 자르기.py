#1부터 max 값 사이에 정답이 있다
# 이진 탐색을 이용 해 정답을 찾아보자
#조건 1. arr-height  ==  M 을 만족시켜야한다

import sys
def binary_search(max_value):
    low =1
    high = max_value

    while(True):
        sum =0
        target = (low + high) // 2

        for i in arr:
            if i - target > 0:
                sum+=i-target
                if sum > M:
                    break

        if sum == M:
            print(target)
            return

        #target의 value는 sum
        if sum > M :
            low = target +1
            if low>high:
                print(target)
                return

        else :
            high = target -1
            if low>high:
                print(target-1)
                return


# 4 12
# 20 15 10 17
# 정답은 13
input= sys.stdin.readline

N,M= map(int,input().split())

arr= list(map(int,input().split()))

h=max(arr)

binary_search(h)