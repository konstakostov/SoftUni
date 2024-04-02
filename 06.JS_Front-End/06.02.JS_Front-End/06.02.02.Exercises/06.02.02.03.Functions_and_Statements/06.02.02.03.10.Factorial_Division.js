function solve(x, y) {
    console.log((factorial(x) / factorial(y)).toFixed(2));

    function factorial(num) {
        let numFactorial = 1;

        for (let i = 1; i <= num; i++) {
            numFactorial *= i;
        }

        return numFactorial;
    }
}

solve(5, 2);
solve(6, 2);