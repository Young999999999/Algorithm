

def solution(video_len, pos, op_start, op_end, commands):
    
    def stringToTime(time):
        t = time.split(':')
        return int(t[0])*60 + int(t[1])
    
    def timeToString(time):
        m = str(time//60)
        s = str(time%60)
        
        if len(m)==1:
            m = "0" + m
        if len(s) == 1:
            s = "0" + s
            
        return m+":"+s
    
    def move(op,now):
    
        if op == "prev":
            now = max(0,now-10)
        elif op == "next":
            now = min(video_len,now+10)
        
        if op_start<=now<=op_end:
            now = op_end
            
        return now

    video_len = stringToTime(video_len)
    op_start = stringToTime(op_start)
    op_end = stringToTime(op_end)
    
    now_t = stringToTime(pos)
    now_t = move("잉",now_t)
    
    for op in commands:
        now_t = move(op,now_t)
        
    return timeToString(now_t)