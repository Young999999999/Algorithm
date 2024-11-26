import sys
from collections import deque

input = sys.stdin.readline

t= int(input())

for i in range(t):
    q = deque()
    op=input().strip()
    num = int(input())
    if num >0:
        arr= input().strip()
        arr= arr[1:-1]
        arr= list(map(int,arr.split(',')))
    else:
        arr=input().strip()
        arr=[]

    for j in arr:
        q.append(j)
    err_bit = 0
    r_bit = 0
    for j in op:
        if j == 'R':
            if r_bit == 0:
                r_bit =1
            else:
                r_bit= 0


        if j == 'D':
            if num ==0:
                err_bit = 1
                continue

            if r_bit == 0 and num > 0:
                x = q.popleft()
                num-=1

            if r_bit == 1 and num >0:
                x = q.pop()
                num -=1

    if err_bit == 1:
        print("error")
    else:

        if len(q) == 0:
            print('[]')
            continue

        if r_bit == 0:
            result= []
            init = 1
            for j in range(len(q)):
                result.append(q.popleft())
            for j in result:
                if init==1:
                    print('[' ,end = '')
                    if len(result) == 1:
                        print(j, end=']')
                        print()
                    else:
                        print(j,end=',')
                else:
                    if init == len(result):
                        print(j,end=']')
                        print()
                    else:
                        print(j,end=',')
                init +=1

        else:
            result = []
            init = 0
            for j in range(len(q)):
                result.append(q.pop())
            for j in result:
                if init == 0:
                    print('[', end='')
                    if len(result) == 1:
                        print(j, end=']')
                        print()
                    else:
                        print(j, end=',')
                else:
                    if init == len(result) - 1:
                        print(j, end=']')
                        print()
                    else:
                        print(j, end=',')
                init += 1
