fs = require('fs');
let [n,...lines] = fs.readFileSync(0,'utf8').trim().split('\n');
let ans = 0;

let dict = {};
for(let line of lines){
    if(line === "ENTER") {
        ans += Object.keys(dict).length; 
        dict = {};
    } else{
        dict[line] = true;
    }
}
ans += Object.keys(dict).length;

console.log(ans)
