fs = require('fs')
let input = fs.readFileSync(0,'utf8').trim().split("\n");
let [n,m] = input[0].split(" ").map(Number);
let input_errors = input[1].split(" ").map(Number);
let [x,y] = input[2].split(" ").map(Number);

let errors  = new Array(m+2);

errors[0] = 0;
errors[m+1] = n+1;

for(let i=1; i<m+1 ;i++){
    errors[i] = input_errors[i-1];
}

function judge(k,x){
    let MAX = -1;
    
    for (let s=1; s<m-k+2; s++){
        let line = errors[s+k] - errors[s-1] - 1
        MAX = Math.max(MAX,line);
    }
    return MAX >= x;
}

let s = y;
let e = m;
for (let i=0;i<20;i++){
    let mid = Math.floor((s+e)/2);

    if(judge(mid, x)) {
       e = mid 
    } else {
        s = mid
    }
}

//Y개 이상 없애면서 X줄 이상 연속하게 만들 수 있는 최소 에러 제거 수
console.log(m-e);
