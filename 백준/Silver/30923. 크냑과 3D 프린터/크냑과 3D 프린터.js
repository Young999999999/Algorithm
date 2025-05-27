let fs = require('fs');
let input = fs.readFileSync(0,'utf-8').trim().split('\n');

let n = +input[0];
let heights = input[1].split(' ').map(Number);


//  변 now의 겉넓이 -> 2+ now*4


//i) 현재값이 이전값보다 같거나 작을 때 -> prevSum - now +  now*3+2  
//ii) 현재값이 이전값보다 클 때 -> prevSum + now -2*prev + now*3 + 2

let prev = 0;
let prevSum = 0;

for(let i=0; i<n; i++){
    let now = heights[i];
    //i)
    if(prev >= now){
        prevSum = prevSum + now*2+2;
    } 
    // ii )
    else {
        prevSum = prevSum -2*prev + now*4 + 2;
    }
    prev = now
}

console.log(prevSum)






