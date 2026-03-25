def findMaxNum(arr):
    MAX = 0
    idx = 0
    for i in arr:
        x,y = i
        if MAX < x:
            MAX = x
            idx = 0
        if MAX < y:
            MAX = y
            idx = 1
            
    return MAX,idx

def solution(sizes):
    MAX,idx = findMaxNum(sizes)
 
    for i in range(len(sizes)):
        w,h = sizes[i]
        if idx == 0:
            if h > w:
                sizes[i] = [h,w]
        else:
            if w > h:
                sizes[i] = [h,w]
    
    if idx == 0:
        sizes.sort(key=lambda x:-x[1])
        return MAX * sizes[0][1]

    if idx == 1:
        sizes.sort(key=lambda x:-x[0])
        return MAX * sizes[0][0]
    return 0