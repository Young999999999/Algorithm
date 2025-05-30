fs = require('fs')
let [n,...lines] = fs.readFileSync(0,'utf8').trim().split("\n");
n = +n
let graph = new Array(n).fill(0).map(() => {
    return [];
});

lines.forEach((v,i) => {
    for(let next = 0; next<n ;next++){
        if(v[next] === 'Y'){
            graph[i].push(next);
        } 
    }
});

let visited = new Array(n).fill(0);
for(let i =0; i<n ;i++){
    visited[i] = new Array(n).fill(0);
}

for (let i=0; i<n ; i++){
    
    //직접 친구
    for(next of graph[i]){
        link(i,next);
    }

    //간접 친구 
    for(first of graph[i]){
        for (second of graph[i]){
            link(first,second);
        }
    }

}

function link(a,b){
    visited[a][b] = 1;
    visited[b][a] = 1;
}

let ans = 0

visited.forEach(e => {
    let sum =0;
    for (let i=0; i< e.length;i++){
        sum += e[i];
    }
    ans = Math.max(ans,sum-1);
})

console.log(ans)