function solve(number) {
    let oddSum = 0;
    let evenSum = 0;

    for (let digit of number.toString()) {
        if (digit % 2 !== 0) {
            oddSum += Number(digit);
        } else {
            evenSum += Number(digit);
        }
    }

    console.log(`Odd sum = ${oddSum}, Even sum = ${evenSum}`)
}

solve(1000435);
solve(3495892137259234);