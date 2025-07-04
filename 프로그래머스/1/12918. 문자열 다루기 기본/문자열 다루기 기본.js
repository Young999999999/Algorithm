function solution(s) {
    const regex = /(^[0-9][0-9][0-9][0-9]$)|(^[0-9][0-9][0-9][0-9][0-9][0-9]$)/
    console.log(regex.test(s))
    if(regex.test(s)){
        return true
    }
    return false 
}