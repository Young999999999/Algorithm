function solution(s) {

    let length = new Array(1001).fill(1000)
    length[1] = s.length
    
    for (let k=1; k<s.length;k++){
        let zip = ''
        let prev =''
        let cnt = 1
        for(let i=0; i<s.length;i+=k){
            let cur = slice(s,i,k)
            
            if(cur === prev){
                cnt++
            } 
            // 카운트가 깨졋다면
            else {
                if(cnt > 1){
                    zip += cnt + prev
                    cnt = 1
                } else{
                    zip += prev
                }
            }
            
            prev = cur
        }
        
        
        if(cnt > 1){
                    zip += cnt + prev
                    cnt = 1
                } else{
                    zip += prev
                }
        
        
        length[k] = zip.length
    }    
    console.log(length)
    let a = length.reduce((min,v) => Math.min(min,v))
 
    return a;
}


function slice(s,idx,k){
    if(idx+k > s.length) return s.slice(idx,s.length)
    
    return s.slice(idx,idx+k)
}