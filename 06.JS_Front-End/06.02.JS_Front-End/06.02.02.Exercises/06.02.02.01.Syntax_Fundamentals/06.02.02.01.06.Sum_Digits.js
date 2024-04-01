function solve(number) {
    let numberString = number.toString();
    let sumDigits = 0;

    for (let i = 0; i < numberString.length; i++) {
        sumDigits += Number(numberString[i]);
    }

    console.log(sumDigits);
}

solve(245678);
solve(97561);
solve(543);