function solution(lottos, win_nums) {
    var answer = [];
    let cnt = 0
    let zeroCnt = 0
    
    for (let num of lottos){
        
        //로또 번호중 하나라면
        if(win_nums.indexOf(num) !== -1){
            cnt++
        } 
        
        if(num === 0){
            zeroCnt++
        }
    }
    console.log(cnt,zeroCnt)
    answer.push(Math.min(6,7-(cnt+zeroCnt)))
    answer.push(Math.min(6,7-cnt))
    
    // 7 - 6 7 -5 
    // 6 5 4 3 2 1 0 
    // 1 2 3 4 5 6 6
    
    return answer;
}