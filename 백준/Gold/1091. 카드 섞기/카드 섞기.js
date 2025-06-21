let fs = require('fs')
let lines = fs.readFileSync(0,'utf8').trim().split('\n')
let n = +lines[0]
let p = lines[1].split(' ').map(Number)
let s = lines[2].split(' ').map(Number)
let flag = 0
let cnt = 0
for (let i=0; i<1000000;i++){
    if(isCorrect()){
        flag = 1
        cnt = i
        break
    }
    suffle()
}

console.log(flag === 0 ? -1 : cnt)

//suffle
function suffle(){
    let tmp = new Array(n).fill(0)
    for (let i=0 ;i<n; i++){
        tmp[s[i]] = p[i]
    }
    p = tmp
}

//isCorrect
function isCorrect(){
    for (let i =0; i<n ;i++){
        let idx = i%3
        if(p[i] === idx){
            continue
        }   
        return false
    }
    return true;
}
