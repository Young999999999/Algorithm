import sys
def solution(n, lost, reserve):
    answer = 0
    students = [0] * (n+1)

    lost.sort()
    
    for i in lost[:]:
        for j in reserve[:]:
            if i==j:
                lost.pop(lost.index(i))
                reserve.pop(reserve.index(i))

    
    for i in lost[:]:
        print(lost,reserve)
        if i-1 in reserve:
            reserve.pop(reserve.index(i-1))
            lost.pop(lost.index(i))
            continue
        
        if i+1 in reserve:
            reserve.pop(reserve.index(i+1))  
            lost.pop(lost.index(i))
    print(lost,reserve)
    return n - len(lost)