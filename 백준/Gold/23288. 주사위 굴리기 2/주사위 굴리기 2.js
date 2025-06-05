fs = require('fs');
lines = fs.readFileSync(0,'utf8').trim().split('\n');

let [n,m,k] = lines[0].split(' ').map(Number);
let matrix = [];
let visited= [];

for(let i=0; i<n;i++){
   let row = new Array(m).fill(0);
   let copy = lines[i+1].split(' ').map(Number);
   for(let j=0;j<row.length;j++){
    row[j] = copy[j]; 
   }
    matrix.push(row);
    visited.push(new Array(m).fill(0));
    
}

let dice = new Array(6).fill(0);
let [r,c] = [0,0];
let vector = [[],[-1,0],[0,1],[1,0],[0,-1]];
let score =0;
let dir = 2;
let size =0;
init(dice);

for(let i=0; i<k;i++){
    //갈 수 있는지 확인
    let [dr,dc] = vector[dir]; 
    let [nr,nc] = [r+dr,c+dc];
    
    //범위 초과라면 이동 방향 반대
    if(!(0<=nr && nr <n && 0<=nc && nc<m)){
        if(dir===1) dir=3;
        else if(dir===3) dir=1;
        else if(dir===2) dir=4;
        else if(dir===4) dir=2;

    }
    
    //다시 갈 위치 설정;
    [dr,dc] = vector[dir]; 
    [nr,nc] = [r+dr,c+dc];

    //주사위 굴리기
    dice = roll(dice,dir);
    
    size = 0;
    for(let j=0;j<n;j++){
        visited[j] = new Array(m).fill(0);
    }
    dfs(nr,nc);
    score += size * matrix[nr][nc];
    [r,c] = [nr,nc];

    // 다음 굴러갈 방향 결정
    dir = rotate(dice[0],matrix[nr][nc],dir);
  
}

console.log(score);

function init(dice) {
    //0 아랫면 1왼쪽 2위 3오른쪽 4 앞 5 뒤
    dice[0] = 6;
    dice[1] = 4;
    dice[2] = 1;
    dice[3] = 3;
    dice[4] = 2;
    dice[5] = 5;
}

function rotate(a,b,dir){
    // dir 1,2,3,4 북,동,남,서
    
    //시계
    if(a>b) {
        dir %=4
        dir += 1 
    } 

    // 반시계
    if(a<b) {
        dir = dir - 1 === 0 ? 4 : dir -1;
    } 

    return dir
}

function roll(dice,dir){
    //동쪽 구르기
    if(dir === 2) {
        let [tmp0,tmp1,tmp2,tmp3] = [dice[0],dice[1],dice[2],dice[3]];
        [dice[0],dice[1],dice[2],dice[3]] = [tmp3,tmp0, tmp1, tmp2];
    }

    //서쪽 구르기 
    if(dir === 4) {
        let [tmp0,tmp1,tmp2,tmp3] = [dice[0],dice[1],dice[2],dice[3]];
        [dice[0],dice[1],dice[2],dice[3]] = [tmp1,tmp2, tmp3, tmp0];
    }

    //북쪽 구르기
    if(dir === 1) {
        let [tmp0,tmp2,tmp4,tmp5] = [dice[0],dice[2],dice[4],dice[5]];
        [dice[0],dice[2],dice[4],dice[5]] = [tmp4,tmp5, tmp2, tmp0];
    }

    //남쪽 구르기
    if(dir === 3) {
        let [tmp0,tmp2,tmp4,tmp5] = [dice[0],dice[2],dice[4],dice[5]];
        [dice[0],dice[2],dice[4],dice[5]] = [tmp5,tmp4, tmp0, tmp2];
    }
    
    return dice;
}

function dfs(r,c){
    visited[r][c] = 1;
    size++;

    for (let i=1; i<5;i++){
        let [dr,dc] = vector[i];
        
        nr = r+dr;
        nc = c+dc;
        if(0<=nr && nr <n && 0<=nc && nc<m) {
            if(!visited[nr][nc] && matrix[nr][nc] === matrix[r][c]){
                dfs(nr,nc);
            }
        }
    }
}
