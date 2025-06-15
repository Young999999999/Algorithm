function solution(today, terms, privacies) {
    var answer = [];
    today = today.split(".").map(Number);
    if(today[2] === 28){
        today[2] = 1
        today[1]++;
        today[0] += Math.floor(today[1]/13);
        today[1] = today[1]%12 === 0 ? 12 : today[1]%12; 
    } else{
        today[2]++;
    }
    
    let itgo = new Map();
    for (let line of terms){
        let [month, period] = line.split(" ");
        itgo.set(month,+period);
    }
    
    let result = [];
    let idx =1;
    for (let line of privacies){
        let [day, kind] = line.split(" ");
        let time = day.split(".").map(Number);
        time[1] += itgo.get(kind);
        time[0] += Math.floor((time[1]-1)/12);
        time[1] = time[1]%12 === 0 ? 12 : time[1]%12;   
    
        
        for(let i =0; i<3; i++){
            if (today[i] > time[i]){
                
                result.push(idx);
                break;
            } else if (today[i] < time[i]){
                break;
            }
        } 
        idx++;
    }
    

    return result;
}