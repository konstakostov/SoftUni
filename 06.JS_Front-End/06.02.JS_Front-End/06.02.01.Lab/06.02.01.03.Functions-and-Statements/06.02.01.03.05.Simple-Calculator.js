function solve(x, y, operator) {
    if (operator === 'multiply') {
        console.log(x * y);
    } else if (operator === 'divide') {
        console.log(x / y);
    } else if (operator === 'add') {
        console.log(x + y);
    } else if (operator === 'subtract') {
        console.log(x - y);
    }
}

solve(5, 5, 'multiply');
solve(40, 8, 'divide');
solve(12, 19, 'add');
solve(50, 13, 'subtract');