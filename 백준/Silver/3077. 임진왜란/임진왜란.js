fs = require('fs');
let [n,...lines] = fs.readFileSync(0,'utf8').trim().split('\n');
let dict = {}

init_dict(lines[0].split(' '))
let [score,size] = gradeWars(lines[1].split(' '))
console.log(score + '/'+size)

function gradeWars(wars){
    let size = 0;
    let score = 0;
    for(let i =0; i<wars.length; i++){
        for(let j =i+1; j<wars.length; j++){
            size++;
            if(dict[wars[i]] < dict[wars[j]]) score++;
        }    
    }

    return [score,size];
}

function init_dict(wars){
    let value = 1;
    for (let war of wars){
        dict[war] = value++;
    }
}
