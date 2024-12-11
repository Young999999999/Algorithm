import sys
input = sys.stdin.readline

infix = input().strip()
stack = []
top=""
high = ["*","/"]
low = ["+","-"]
bit = 0
for i in infix:
    if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print(i,end= '')

    else: #연산자일 때

        if i == ")":

            while stack:
                op = stack.pop()
                if op == '(':
                    break
                print(op,end='')
            continue

        elif i == '(':
            stack.append('(')
            continue
        elif i in high:
            while (stack and stack[-1] !='(' and (stack[-1] =='*' or stack[-1] =='/')):
                op=stack.pop()
                print(op,end='')
        else: #연산자가 low
            while stack and stack[-1] != '(':
                op = stack.pop()
                print(op, end='')


        stack.append(i)

while stack:
    op = stack.pop()
    print(op, end='')