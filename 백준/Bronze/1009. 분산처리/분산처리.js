let fs = require('fs')
let [T, ...inputs] = fs.readFileSync(0, 'utf8').trim().split('\n')

T = +T
inputs = inputs.map((input) => input.split(' ').map(Number))

inputs.forEach((input) => {
    const [a, b] = input
    const options = []
    let i = 1
    while (1) {
        let num = (a ** i).toString()
        num = num[num.length - 1]
        if (options.includes(num)) {
            break
        }
        options.push(num)
        i++
    }

    let result
    if (!(b % options.length)) {
        result = options[options.length - 1]
    } else {
        result = options[b % options.length - 1]
    }

    console.log(result === '0' ? 10 : result)
})