function solution(dartResult) {
    let answer = 0;
    let chances = []
    let tmp = []
    for (let v of dartResult){
        if('SDT'.includes(v)){
            tmp.push(v)
            chances.push(tmp)
            tmp = []
        } else if('0123456789'.includes(v)) {
            
            if(v === '0' && tmp[tmp.length-1] === '1'){
                tmp[tmp.length-1] = tmp[tmp.length-1].concat(v)
                continue
            }
          tmp.push(v)
        } else {
            chances[chances.length-1].push(v)
        }
    }
    

    let score = []
    
    for(let op of chances){
        for (let v of op){
            if ('0123456789'.includes(v) || v === '10') score.push(Number(v))
        
            if('*' === v){
                star(score)
            }
            if('#' === v){
                acha(score)
            }

            if('S' === v){
                score[score.length-1] = score[score.length-1]
            }

            if('D' === v){
                score[score.length-1] = score[score.length-1] ** 2
            }

            if('T' === v){
                score[score.length-1] = score[score.length-1] ** 3
            }    
            console.log(v ,' ', score)
        }
    
    }
    answer = score.reduce((sum,cur) => sum+cur)
    
    return answer;
}

function star(score){
    score[score.length - 1] = 2 * score.at(-1) 
    if(score.at(-2)){
        score[score.length - 2] = 2 * score.at(-2)
    }
    return score
}

function acha(score){
    score[score.length - 1] =  -1 * score.at(-1) 
    
    return score
}