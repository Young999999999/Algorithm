fs = require('fs');

function solve(){
    let lines = fs.readFileSync(0,'utf8').trim().split('\n');
    let n = +lines[0];
    let dict = new Map();

    for (let i=1;i<=n;i++){
        let [me,mn] = lines[i].split(' ');    
        dict.set(me,mn);
    }

    let m = +lines[n+1];
    let result = '';

    for (let i=0; i<m; i++){
        let input = lines[n+2+i].split(' ');
        let tmp = [];
        for(let x of input.slice(1)){
            if(dict.get(x)){
                tmp.push(dict.get(x));
            } else{
                console.log('YOU DIED');
                tmp = [];
                break;
            }
        }

        if(tmp.length > 0){
            console.log(tmp.join(' '));
        }
    }
}

solve();
