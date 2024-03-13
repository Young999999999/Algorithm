import sys
input = sys.stdin.readline

def getMid(color):
    return (color[0] + color[1])/2

def getDir(std, s, e):
    mid = (s+e)/2
    if std > mid:
        return 'R'

    else:
        return 'L'


def setChange(dir,std,color):

    if dir == 'R':
        if color[0] > std:
            color[0] = std - (color[0] - std)
        if color[1] > std:
            color[1] = std - (color[1] - std)

    if dir == 'L':
        if color[0] <= std:
            color[0] = std + (std - color[0])
        if color[1] <= std:
            color[1] = std + (std - color[1])


size = int(input())

red= list(map(float,input().split()))
blue = list(map(float,input().split()))
yellow = list(map(float,input().split()))


s = 0
e = size
std = getMid(red)

dir = getDir(std,s,e)
if dir == 'R' :

    setChange(dir,std, blue)
    setChange(dir,std,yellow)
    size = size - (e - std)
    e = std

else:
    setChange(dir,std, blue)
    setChange(dir,std ,yellow)
    size = size - (std - s)
    s = std

if blue[0] != blue[1] :
    std = getMid(blue)
    dir = getDir(std,s,e)
    if dir == 'R':
        setChange(dir,std, yellow)
        size = size - (e - std)
        e = std

    else:
        setChange(dir,std, yellow)
        size = size - (std - s)
        s = std

if yellow[0] != yellow[1]:
    std = getMid(yellow)
    dir = getDir(std, s, e)
    if dir == 'R':
        size = size - (e - std)
        e = std

    else:
        size = size - (std - s)
        s = std

result = round(size + 1e-9,1)
print(result)




