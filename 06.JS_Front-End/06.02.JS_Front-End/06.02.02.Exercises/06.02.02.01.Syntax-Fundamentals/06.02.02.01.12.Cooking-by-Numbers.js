function solve(number, ...operations) {
    let resultNumber = number;

    operations.forEach(operation => {
        switch (operation) {
            case 'chop':
                resultNumber /= 2;
                break
            case 'dice':
                resultNumber = Math.sqrt(resultNumber);
                break
            case 'spice':
                resultNumber += 1;
                break
            case 'bake':
                resultNumber *= 3;
                break
            case 'fillet':
                resultNumber *= (1 - 0.20);
                break
        }

        console.log(resultNumber);
    })
}

solve('32', 'chop', 'chop', 'chop', 'chop', 'chop');
solve('9', 'dice', 'spice', 'chop', 'bake', 'fillet');