function largestCase(num01, num02, num03) {
    let result;

    if (num01 > num02 && num01 > num03) {
        result = num01;
    } else if (num02 > num01 && num02 > num03) {
        result = num02;
    } if (num03 > num02 && num03 > num01) {
        result = num03;
    }

    console.log(`The largest number is ${result}`)
}

largestCase(5, -3, 16)
largestCase(-3, -5, -22.5)
