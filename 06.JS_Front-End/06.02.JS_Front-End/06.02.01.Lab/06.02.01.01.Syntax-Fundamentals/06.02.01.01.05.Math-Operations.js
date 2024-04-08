function solve(num01, num02, operator) {
    if (operator === '+') {
        console.log(num01 + num02);
    } else if (operator === '-') {
        console.log(num01 - num02);
    } else if (operator === '*') {
        console.log(num01 * num02);
    } else if (operator === '/') {
        console.log(num01 / num02);
    } else if (operator === '%') {
        console.log(num01 % num02);
    } else if (operator === '**') {
        console.log(num01 ** num02);
    }
}

solve(5, 6, '+');
solve(3, 5.5, '*');