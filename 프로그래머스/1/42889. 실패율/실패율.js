function solution(N, stages) {
    var answer = [];
    let cnt = new Array(N+2).fill(0)
    let clearCnt = new Array(N+2).fill(0)
    for (let stage of stages){
        for (let i=0; i< stage; i++){
            cnt[i]++
            clearCnt[i]++
        }
        cnt[stage]++
    }
    
    console.log(cnt)
    console.log(clearCnt)
    
    let failRate = []
    for (let i=1; i<N+1; i++){
        if(cnt[i] === 0){
            failRate.push(0)
            continue
        }
        
        failRate.push((cnt[i]-clearCnt[i])/cnt[i])
    }
    
    console.log(failRate)
    
    let failRateRank = [...failRate].sort((a,b) => {
        if (a !== b) return -1*(a-b)  
            
    })
    
    
    console.log(failRateRank)
    visited=new Array(N+2).fill(0)
    
    for (let rank of failRateRank){
        //answer.push(failRate.indexOf(rank)+1)
        
        for (let i=0; i<N;i++){
            if(!visited[i] && failRate[i] === rank){
                visited[i] = 1
                answer.push(i+1)
                break
            } 
        }
    }
    
    
    return answer;
}