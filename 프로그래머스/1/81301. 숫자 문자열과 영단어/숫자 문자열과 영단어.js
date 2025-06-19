function solution(s) {
  
    function init(){
        dict.set('zero','0')
        dict.set('one','1')
        dict.set('two','2')
        dict.set('three','3')
        dict.set('four','4')
        dict.set('five','5')
        dict.set('six','6')
        dict.set('seven','7')
        dict.set('eight','8')
        dict.set('nine','9')
    }
    
    let dict  = new Map()
    init()

    let answer = ''
    let string = ''
    for(let c of s.split('')){
        if(c in ['0','1','2','3','4','5','6','7','8','9']){
            answer += c
        } else{
            string += c
            if(dict.get(string)){
                answer += dict.get(string)
                string = ''
            }
        }
    }
    
    console.log(answer)
    return Number(answer)
    
}