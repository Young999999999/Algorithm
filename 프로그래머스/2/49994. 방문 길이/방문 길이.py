def solution(dirs):
    x,y =0,0
    visited=[[[False for i in range(11)] for j in range(11)] for k in range(4)]
    
    def move(dir,x,y):
        if dir == 'U':
            y = y+1
        if dir == 'D':
            y = y-1
        if dir == 'L':
            x = x-1
        if dir == 'R':
            x = x+1
            
        bit = 0
        if -5<=x<=5 and -5 <=y<=5:
            bit = 1
        
        return x,y,bit
    
    def reverseDir(dir):
        if dir ==0:
            return 1
        if dir ==1:
            return 0
        if dir == 2:
            return 3
        if dir == 3:
            return 2
    
    
    answer = 0
    for i in dirs:
        mx,my,bit = move(i,x,y)
        
        if bit == 1 :
            dir = 0
            if i =="U":
                dir = 0
            if i== "D":
                dir = 1
            if i == "L":
                dir = 2
            if i == "R":
                dir = 3
            if not visited[dir][y][x] and not visited[reverseDir(dir)][my][mx]:
                answer+=1
            visited[dir][y][x] = True
    
            x,y = mx,my
            dir = reverseDir(dir)
            visited[dir][y][x] = True
            
            
            
        
    
    
            
    return answer