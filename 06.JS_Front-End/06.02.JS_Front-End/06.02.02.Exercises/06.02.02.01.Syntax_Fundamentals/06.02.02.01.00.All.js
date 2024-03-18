// 01. Ages
function solve_age(age) {
    if (age >= 0 && age <= 2) {
        console.log('baby');
    } else if (age >= 3 && age <= 13) {
        console.log('child');
    } else if (age >= 14 && age <= 19) {
        console.log('teenager');
    } else if (age >= 20 && age <= 65) {
        console.log('adult');
    } else if (age >= 66) {
        console.log('elder');
    } else {
        console.log('out of bounds')
    }
}

solve_age(20)
solve_age(1)
solve_age(100)
solve_age(-1)


// 02. Vacation
function solve_vacation(groupSize, groupType, day) {
    let singlePrice = 0

    if (day === 'Friday') {
        switch (groupType) {
            case 'Students':
                singlePrice = 8.45;
                break;
            case 'Business':
                singlePrice = 10.90;
                break;
            case 'Regular':
                singlePrice = 15;
                break;
        }
    } else if (day === 'Saturday') {
        switch (groupType) {
            case 'Students':
                singlePrice = 9.80;
                break;
            case 'Business':
                singlePrice = 15.60;
                break;
            case 'Regular':
                singlePrice = 20;
                break;
        }
    } else if (day === 'Sunday') {
        switch (groupType) {
            case 'Students':
                singlePrice = 10.46;
                break;
            case 'Business':
                singlePrice = 16;
                break;
            case 'Regular':
                singlePrice = 22.50;
                break;
        }
    }

    let totalPrice = groupSize * singlePrice

    if (groupType === 'Students' && groupSize >= 30) {
        totalPrice = totalPrice * (1 - 0.15)
    } else if (groupType === 'Business' && groupSize >= 100) {
        totalPrice = totalPrice - (10 * singlePrice)
    } else if (groupType === 'Regular' && groupSize >= 10 && groupSize <= 20) {
        totalPrice = totalPrice * (1 - 0.05)
    }

    console.log('Total price: ' + totalPrice.toFixed(2))
}

solve_vacation(
    30,
    "Students",
    "Sunday"
)

solve_vacation(
    40,
    "Regular",
    "Saturday"
)


// 03. Leap Year
function solveLeapYear(year) {
    if ((year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0)) {
        console.log('yes')
    } else {
        console.log('no')
    }
}

solveLeapYear(1984)
solveLeapYear(2003)
solveLeapYear(4)


// 04. Print and Sum
function solvePrintAndSum(startNumber, endNumber) {
    let usedNumbers = []
    let totalSum = 0

    for (let i = startNumber; i <= endNumber; i++) {
        totalSum = totalSum + i;
        usedNumbers.push(i)

    }

    console.log(usedNumbers.join(' '))
    console.log('Sum: ' + totalSum)
}

solvePrintAndSum(5, 10)
solvePrintAndSum(0, 26)
solvePrintAndSum(50, 60)


// 05. Multiplication Table
function solveMultiplicationTable(num) {
    for (let i = 1; i <= 10; i++) {
        console.log(`${num} X ${i} = ${num * i}`)
    }
}

solveMultiplicationTable(5)
solveMultiplicationTable(2)


// 06. Sum Digits
function solveSumDigits(num) {
    num = String(num);
    let totalSum = 0;

    for (let i = 0; i < num.length; i++) {
        totalSum += parseInt(num[i])
    }

    console.log(totalSum)
}

solveSumDigits(245678)
solveSumDigits(97561)
solveSumDigits(543)


// 07. Chars to String
function solveCharsToStrings(char01, char02, char03) {
    console.log(char01 + char02 + char03)
}

solveCharsToStrings(
    'a',
    'b',
    'c'
)

solveCharsToStrings(
    '%',
    '2',
    'o'
)

solveCharsToStrings(
    '1',
    '5',
    'p'
)


// 08. Reversed Chars
function solveReversedChars(char01, char02, char03) {
    let normalString = char01 + char02 + char03
    let reverseString = normalString.split('').reverse().join(' ')

    console.log(reverseString)
}

solveReversedChars(
    'A',
    'B',
    'C'
)

solveReversedChars(
    '1',
    'L',
    '&'
)


// 09. Fruit
function solveFruit(fruitType, fruitWeightInGrams, pricePerKilogram) {
    let gramsToKilograms = fruitWeightInGrams / 1000
    let money = gramsToKilograms * pricePerKilogram

    console.log(`I need \$${money.toFixed(2)} to buy ${gramsToKilograms.toFixed(2)} kilograms ${fruitType}.`)
}

solveFruit('orange', 2500, 1.80)
solveFruit('apple', 1563, 2.35)


// 10. Same Numbers
function solveSameNumbers(num) {
    let numAsString = String(num);
    let numSum = 0;
    let sameNumbers = true;
    let lastChar = '';

    for (let i = 0; i < numAsString.length; i++) {
        numSum += parseInt(numAsString[i]);

        if (lastChar === '') {
            lastChar = numAsString[i];
        } else {
            if (lastChar !== numAsString[i]) {
                sameNumbers = false;
            }
        }
    }

    console.log(sameNumbers)
    console.log(numSum)
}

solveSameNumbers(2222222)
solveSameNumbers(1234)


// 11. Road Radar
function solveRoadRadar(speed, area) {
    let motorwayLimit = 130;
    let interstateLimit = 90;
    let cityLimit = 50;
    let residentialLimit = 20;

    let withinSpeedLimit = true;
    let speedLimitZone = 0;

    switch (area) {
        case 'motorway':
            speedLimitZone = motorwayLimit;
            if (speed > motorwayLimit) {
                withinSpeedLimit = false;
            }
            break;
        case 'interstate':
            speedLimitZone = interstateLimit;
            if (speed > interstateLimit) {
                withinSpeedLimit = false;
            }
            break;
        case 'city':
            speedLimitZone = cityLimit;
            if (speed > cityLimit) {
                withinSpeedLimit = false;
            }

            break;
        case'residential':
            speedLimitZone = residentialLimit;
            if (speed > residentialLimit) {
                withinSpeedLimit = false;
            }
            break;
    }

    if (withinSpeedLimit === true) {
        console.log(`Driving ${speed} km/h in a ${speedLimitZone} zone`)
    } else {
        let speedDifference = speed - speedLimitZone;
        let status = null;

        if (speedDifference <= 20) {
            status = 'speeding';
        } else if (speedDifference <= 40) {
            status = 'excessive speeding'
        } else {
            status = 'reckless driving'
        }

        console.log(`The speed is ${speedDifference} km/h faster than the allowed speed of ${speedLimitZone} - ${status}`)
    }
}

solveRoadRadar(40, 'city')
solveRoadRadar(21, 'residential')
solveRoadRadar(120, 'interstate')
solveRoadRadar(200, 'motorway')


// 12. Cooking by Numbers
function solveCookingByNumbers(num, ...args) {
    let operationResult = num

    for (const operation of args) {
        switch (operation) {
            case 'chop':
                operationResult /= 2;
                console.log(operationResult);
                break;
            case 'dice':
                operationResult = Math.sqrt(operationResult);
                console.log(operationResult);
                break;
            case 'spice':
                operationResult += 1;
                console.log(operationResult);
                break;
            case 'bake':
                operationResult *= 3;
                console.log(operationResult);
                break;
            case 'fillet':
                operationResult *= (1 - 0.20);
                console.log(operationResult);
                break;
        }
    }
}

solveCookingByNumbers('32', 'chop', 'chop', 'chop', 'chop', 'chop');
console.log('');
solveCookingByNumbers('9', 'dice', 'spice', 'chop', 'bake', 'fillet');

