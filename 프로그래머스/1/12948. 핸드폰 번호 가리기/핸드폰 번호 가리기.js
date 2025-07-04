function solution(phone_number) {
    var answer = '';
    
    let f = phone_number.slice(0,phone_number.length-4)
    let b = phone_number.slice(phone_number.length-4)
    
    return '*'.repeat(f.length) + b

}