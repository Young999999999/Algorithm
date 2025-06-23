function solution(board, moves) {
    
    //인형 뽑았을 때 빈 블록 못 뽑음
    //인형 뽑았을 때 뽑은애랑 리스트 맨 위에있는 애랑 비교.
    let answer = 0
    let stack = []
    
    function custom_catch(line){
        line = line - 1
        
        for (let i =0; i < board.length; i++){
            let doll = board[i][line]
            
            if(doll){
                board[i][line] = 0
                stack.push(doll)
                return doll
            }
        }
    }
    
    for (let line of moves){
        custom_catch(line)
            
        if(stack.length > 1){
            let last = stack[stack.length-1]
            let pre = stack[stack.length-2]
            console.log(last,pre)
            //사라지기
            if(last === pre){
                answer += 2
                stack.pop()
                stack.pop()
            }
        }
    }
    
    return answer;
}