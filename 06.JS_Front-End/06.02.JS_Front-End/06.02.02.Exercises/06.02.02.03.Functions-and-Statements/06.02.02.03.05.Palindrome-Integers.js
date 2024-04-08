function solve(inputArray) {
    inputArray.forEach(digit => {
        let numberNormal = digit.toString().split('');
        let numberReversed = digit.toString().split('').reverse();

        if (Number(numberNormal.join('')) === Number(numberReversed.join(''))) {
            console.log('true');
        } else {
            console.log('false');
        }
    })
}

solve([123,323,421,121]);
solve([32,2,232,1010]);