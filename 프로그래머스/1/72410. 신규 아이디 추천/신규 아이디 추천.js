// len -> 3~15
// 소문자,숫자,-,_,.
//  .. 처음과 끝에 불가능 연속도 불가능
function solution(new_id) {
    var answer = '';
    //step1
    new_id = new_id.toLowerCase()
    
    //step2
    let str= []
    let character = 'abcdefghijklmnopqrstuvwxyz0123456789'.split('').concat(['-','_','.'])
    
    for(let c of new_id){
        if (character.indexOf(c) !== -1){
            str.push(c)
        }    
    }
    new_id = str
    str = [new_id[0]]
    console.log(new_id)
    
    //step3
    for(let i = 1; i<new_id.length; i++){
        if(new_id[i-1] === '.' && new_id[i] === '.'){
            continue
        }
        str.push(new_id[i])
    }
    
    new_id  = str
    console.log(new_id)
    //step4
    new_id = new_id[0] === '.' ? new_id.slice(1) : new_id
    new_id = new_id[new_id.length-1] === '.' ? a(): new_id
     
    function a(){
        new_id.splice(new_id.length-1,1)
        return new_id
    }
    new_id = new_id.join('')
     console.log(new_id)
    
    //step5
    if(new_id.length === 0){
        new_id = 'a'
    }
     console.log(new_id)
    
    //step6
    if(new_id.length >= 16){
        new_id = new_id.slice(0,15)
        new_id = new_id[new_id.length-1] === '.' ? new_id.slice(0,new_id.length-1) : new_id
    }
     console.log(new_id)
    
    //step7
    if(new_id.length <= 2){
        new_id = new_id + new_id[new_id.length-1] + new_id[new_id.length-1]
        new_id = new_id.slice(0,3)
    }
     console.log(new_id)
    
    return new_id;
}
