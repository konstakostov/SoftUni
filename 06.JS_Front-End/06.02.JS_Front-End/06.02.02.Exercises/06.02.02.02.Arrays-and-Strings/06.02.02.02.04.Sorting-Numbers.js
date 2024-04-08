function solve(inputArray) {
    let finalArray = [];
    let startArray = inputArray.sort((a, b) => a - b);

    while (startArray.length > 0) {
        const firstElement = startArray.shift();
        const secondElement = startArray.pop();

        if (firstElement) {
            finalArray.push(firstElement);
        }
        if (secondElement) {
            finalArray.push(secondElement);
        }
    }

    return finalArray;
}

solve([1, 65, 3, 52, 48, 63, 31, -3, 18, 56]);