function solve(number) {
    const numberString = number.toString();
    let isSame = true;
    let numbersSum = 0;

    for (let i = 0; i < numberString.length; i++) {
        if (numberString[i] !== numberString[i + 1] && i + 1 < numberString.length) {
            isSame = false;
        }

        numbersSum += Number(numberString[i]);
    }

    console.log(isSame);
    console.log(numbersSum);
}

solve(2222222);
solve(1234);