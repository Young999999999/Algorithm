fs = require('fs');
let [n,...lines] = fs.readFileSync(0,'utf8').trim().split('\n');
let ans = 0;

let dict = new Map();

for(let line of lines){
    if (line === "ENTER") {
        ans += dict.size;
        dict.clear();
    } else {
        dict.set(line,true);
    }
}

ans += dict.size;
console.log(ans);