fs = require('fs');
let [dn,oven,pizza]= fs.readFileSync(0,'utf8').trim().split("\n");
let [d,n] = dn.split(" ");
oven = oven.split(" ").map(Number);
pizza = pizza.split(" ").map(Number);
let limit = new Array(+d);
MIN = 1000000001

oven.forEach((v,idx) => {
    MIN = Math.min(MIN,v);
    limit[idx] = MIN;
})
limit.push(1000000001);

let end = +d;
let bit =0;
for(p of pizza){
    let s=0;
    if(limit[s] < p || limit[s] === 1000000001){
        bit=1;
        break;
    }
    let e=end;
    for (let i=0; i<20; i++){
        mid = Math.floor((s+e)/2);       
        if(p <= limit[mid]) s = mid;
        else e = mid
    }
   //console.log(limit[s])
    end = s;
    limit[end] = 1000000001;
}

console.log(bit === 1 ? 0 : end+1);