function solution(participant, completion) {
  
    map = new Map()
    for (let name of completion){
        map.set(name,(map.get(name)?? 0) + 1)
    }
    
    for(let name of participant){
        if(map.get(name) > 0){
            map.set(name,map.get(name) -1)
            continue 
        }
        return name 
    }


}