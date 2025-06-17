function solution(id_list, report, k) {
    let answer = new Array(id_list.length).fill(0);
    
    let dict = new Map()
    let idx = new Map()
    let i=0;
    for( let id of id_list){
        idx.set(id,i++)
        dict.set(id,new Map())
    }
    
    for (let line of report){
        let [n1,n2] = line.split(" ")
        dict.get(n2).set(n1,0)
    }
    
    for (let id of dict.keys()){
        if(dict.get(id).size >= k){
            for(let name of dict.get(id).keys()){
                answer[idx.get(name)]++
            }
        }
    }
    
    
//     set.(arr[1],arr[0])
//     .get(arr[1]).set(arr[0])
    
    
    
    return answer;
}