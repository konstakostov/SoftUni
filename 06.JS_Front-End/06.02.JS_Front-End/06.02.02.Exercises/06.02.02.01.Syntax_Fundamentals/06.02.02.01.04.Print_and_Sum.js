function solve(start, end) {
    let numbersString = '';
    let numbersSum = 0;

    for (let i = start; i <= end; i++) {
        numbersString += `${i} `
        numbersSum += Number(i);
    }

    console.log(numbersString.trim());
    console.log(`Sum: ${numbersSum}`);
}

solve(5, 10);
solve(0, 26);