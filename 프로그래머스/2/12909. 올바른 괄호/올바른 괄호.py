def solution(s):
    answer = True
    
    open = []
    
    
    for i in s:
        if i == ')':
            if len(open) == 0:
                return False
            else: open.pop()
        
        else:
            open.append('(')
    
    
    if len(open) > 0:
        return False
        
    return True