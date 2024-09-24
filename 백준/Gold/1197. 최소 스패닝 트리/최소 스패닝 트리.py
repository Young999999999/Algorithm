import sys
input = sys.stdin.readline

def find(x):
    if node[x] == x: #대표수라면
        return x

    node[x] = find(node[x])
    return node[x]

def merge(a,b):
    a = find(a)
    b = find(b)

    if a!=b:
        big,small = max(a,b),min(a,b)
        node[small] = big
        return True
    return False

v,e = map(int,input().split())
node =[i for i in range(v+1)]
graph = [list(map(int,input().split())) for i in range(e)]
graph.sort(key=lambda x:x[2])
cost = 0

for a,b,c in graph:
    if merge(a,b):
       cost += c

root = find(1)
bit = True
for i in range(1,v+1):
    if root != find(i):
        bit = False

if bit:
    print(cost)
else:
    print(0)
