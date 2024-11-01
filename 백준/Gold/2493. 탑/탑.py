# i) bottom 보다 크다면 스택을 비움
# ii) 아니라면 스택에 넣으면서 나보다 작은 놈들 없애버림

n = int(input())
tower = list(map(int,input().split()))
stack = []
bottom = 0

for idx,item in enumerate(tower):
    # i)
    if bottom <= item:
        stack = [(idx,item)]
        bottom = item
        print(0,end=' ')
    # ii)
    else:
        while stack:
            topIdx,top = stack.pop()

            if not item >= top:
                stack.append((topIdx,top))
                stack.append((idx,item))
                print(topIdx+1,end=' ')
                break
