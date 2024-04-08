function solve(...numbers) {
    let negativeCounter = 0;

    numbers.forEach(num => {
        if (num < 0) {
            negativeCounter += 1;
        }
    })

    if (negativeCounter % 2 === 0) {
        console.log('Positive');
    } else {
        console.log('Negative');
    }
}

solve(5, 12, -15);
solve(-6, -12, 14);
solve(-1, -2, -3);