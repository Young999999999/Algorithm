function solution(survey, choices) {
    var result = '';
    
    let choiceScore = [0,3,2,1,0,1,2,3]
    let score = new Map()
    init()
    
    // choices가 1,2,3 인 경우에 앞에 거의 점수를 올림
    // choices가 5,6,7 인 경우에 뒤에 거의 점수를 올림 
    for (let i = 0; i<choices.length; i++){
        let choice = choices[i];
        let [a,b] = survey[i].split('');
        
        if (choice > 4){
            let now = score.get(b);
            score.set(b,now+ choiceScore[choice]);
        } else if (choice <4){
            let now = score.get(a);
            score.set(a,now+ choiceScore[choice]);
        }
    }
    
    result += makeResult('R','T');
    result += makeResult('C','F');
    result += makeResult('J','M');
    result += makeResult('A','N');
    
    function init(){
        score.set('T',0);
        score.set('R',0);
        score.set('C',0);
        score.set('F',0);
        score.set('J',0);
        score.set('M',0);
        score.set('A',0);
        score.set('N',0); 
    }
    
    function makeResult(R,T){
        if (score.get(R) < score.get(T)) {
            return T
        } else{
        return R
        }  
    }
    
    return result;
    
    
    
}