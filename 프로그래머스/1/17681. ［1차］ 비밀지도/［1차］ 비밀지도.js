function solution(n, arr1, arr2) {
    var answer = [];
    let matrix1 = new Array(n).fill(0).map(() => [])
    let matrix2 = new Array(n).fill(0).map(() => [])
    let matrix = new Array(n).fill(0).map(() => [])
    
    for (let i =0; i<n;i++){
        let num = arr1[i]
        
        for(let j=0; j<n;j++){
            if((num & 1) === 1){
                matrix1[i].push('#')
            } else{
                matrix1[i].push(' ')
            }
            num = num >> 1
        }
    }
    
    for (let i =0; i<n;i++){
        let num = arr2[i]
        
        for(let j=0; j<n;j++){
            if((num & 1) === 1){
                matrix2[i].push('#')
            } else{
                matrix2[i].push(' ')
            }
            num = num >> 1
        }
    }
    
    
    console.log(matrix1)
    console.log(matrix2)
    
    for(let i=0; i<n; i++){
        for(let j=0; j<n; j++){
            if(matrix2[i][j] === '#' || matrix1[i][j] === '#'){
                matrix[i].push('#')
            }else{
                matrix[i].push(' ')
            }
        }
        matrix[i] = matrix[i].reverse()
    }
    
    for(let i of matrix){
        answer.push(i.join(''))    
    }
    
    return answer;
}