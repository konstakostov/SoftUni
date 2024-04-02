function solve(number) {
    let digitsSum = 0;
    let result = '';

    if (number > 0) {
        for (let i = 1; i < number; i++) {
            if (number % i === 0) {
                digitsSum += i;
            }
        }
    } else {
        result = 'It\'s not so perfect.';
    }

    if (result.length === 0 && digitsSum === number) {
        result = 'We have a perfect number!';
    } else {
        result = 'It\'s not so perfect.';
    }

    console.log(result);
}

solve(6);
solve(28);
solve(1236498);