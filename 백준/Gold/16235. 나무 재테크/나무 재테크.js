let fs = require('fs')
let lines = fs.readFileSync(0,'utf8').trim().split("\n")
let [n,m,k] = lines[0].split(' ').map(Number)
let vector = [[-1,0],[1,0],[0,-1],[0,1],[1,1],[1,-1],[-1,1],[-1,-1]]
let A = []
let matrix = []
let tree = new Array(n).fill(0).map(() => new Array(n).fill(0).map(() => new Array(0)))
for (let i=1; i<n+1 ;i++){
    A.push(lines[i].split(' ').map(Number))
    matrix.push(new Array(n).fill(5))
}

for (let i=n+1;i<lines.length;i++){
    let [r,c,age] = lines[i].split(" ").map(Number)
    tree[r-1][c-1].push(age)
}

for(let i=0; i<k; i++){
    // console.log("step: ", i)
    // console.log(tree)
    // console.log(matrix)
    springAndSummer()
    fall()
    winter()
}

console.log(calResult())

function springAndSummer() {
    for (let y=0; y<n; y++){
        for (let x=0; x<n ;x++){
            tree[y][x].sort((a,b) => a-b)
            let tmp =[]
            let dead = []
            for (let age of tree[y][x]){
                // 양분 냠냠
                if (age <= matrix[y][x]){
                    matrix[y][x] -= age
                    tmp.push(age+1)
                } else{
                    dead.push(age)
                }
            }
            tree[y][x] = tmp

            //summer
            for (let v of dead){
                matrix[y][x] += Math.floor(v/2)
            }
        }
    }
}

function fall() {
     for (let y=0; y<n; y++){
        for (let x=0; x<n ;x++){
            for (let age of tree[y][x]){
                if(age % 5 === 0){
                    for(let i=0; i<vector.length;i++){
                        let [dx,dy] = vector[i]
                        let [nx,ny] = [x+dx,y+dy]

                        if(0<=nx && nx<n && 0<=ny && ny<n){
                            tree[ny][nx].push(1)
                        }
                    }
                }
            }
        }
    }
}

function winter() {
    for (let y=0; y<n; y++){
        for (let x=0; x<n ;x++){
            matrix[y][x] += A[y][x]
        }
    }
}

function calResult() {
    let result = 0
    for (let y=0; y<n; y++){
        for (let x=0; x<n ;x++){
            result += tree[y][x].length
        }
    } 
    return result
}