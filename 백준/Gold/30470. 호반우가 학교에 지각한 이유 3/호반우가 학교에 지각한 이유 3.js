fs = require('fs')
let lines = fs.readFileSync(0,'utf8').trim().split('\n');
let OPS = lines.slice(1);
let sum = 0;
let longest = 0;
let longestList = [];

for (let i=0; i< OPS.length ; i++){
     let [op,value] = OPS[i].split(' ').map(Number);

      if(op === 2){
          longest = Math.max(longest-value,0);
          longestList.push(longest);
        } else if(op === 1){
            longest = Math.max(longest,value);
        }
}

longest = 1e10;
while(OPS.length){
    let[op, value] = OPS.pop().split(' ').map(Number);
    if(op === 2){
      longest = Math.min(longestList.pop(),longest);
    } else if(op === 1){
        sum += Math.min(longest,value);
    }
}

console.log(sum);