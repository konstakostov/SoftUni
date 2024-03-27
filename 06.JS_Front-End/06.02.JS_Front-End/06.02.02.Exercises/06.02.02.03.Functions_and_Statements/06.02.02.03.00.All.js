// 01. Smallest of Three Numbers;
function solveSmallestInteger(...int) {
    let smallestInteger = Number.MAX_SAFE_INTEGER;

    int.forEach(item => {
        if (item < smallestInteger) {
            smallestInteger = item;
        }
    })

    console.log(smallestInteger);
}

solveSmallestInteger(2, 5, 3);
solveSmallestInteger(600, 342, 123);
solveSmallestInteger(25, 21, 4);
solveSmallestInteger(2, 2, 2);


// 02. Add and Subtract;
function solveAddSubtract(a, b, c) {
    console.log(solveSubtract(solveAdd(a, b), c));

    function solveAdd(a, b) {
        return a + b;
    }

    function solveSubtract(numSum, c) {
        return numSum - c;
    }
}

solveAddSubtract(23, 6, 10);
solveAddSubtract(1, 17, 30);
solveAddSubtract(42, 58, 100);


// 03. Characters in Range;
function solveCharactersInRange(charFirst, charSecond) {
    let charArray = [];

    let smallerAscii = 0;
    let biggerAscii = 0;

    if (charFirst.charCodeAt(0) <= charSecond.charCodeAt(0)) {
        smallerAscii = charFirst.charCodeAt(0);
        biggerAscii = charSecond.charCodeAt(0);
    } else {
        smallerAscii = charSecond.charCodeAt(0);
        biggerAscii = charFirst.charCodeAt(0);
    }

    for (let i = smallerAscii + 1; i < biggerAscii; i++) {
        charArray.push(String.fromCharCode(i))
    }

    console.log(charArray.join(' '))
}

solveCharactersInRange('a', 'd');
solveCharactersInRange('#', ':');
solveCharactersInRange('C', '#');


// 04. Odd and Even Sum;
function solveOddEvenSum(number) {
    let oddSum = 0;
    let evenSum = 0;

    const digits = number.toString().split('').map(Number);

    digits.forEach(digit => {
        if (digit % 2 === 0) {
            evenSum += digit;
        } else {
            oddSum += digit;
        }
    })

    console.log(`Odd sum = ${oddSum}, Even sum = ${evenSum}`)
}

solveOddEvenSum(1000435);
solveOddEvenSum(3495892137259234);


// 05. Palindrome Integers;
function solvePalindromeIntegers(intArray) {
    intArray.forEach(intNumber => {
        console.log(palindromeCheck(intNumber));
    })

    function palindromeCheck(number) {
        const normalNumber = number.toString();
        const reversedNumber = normalNumber.split('').reverse().join('');

        return normalNumber === reversedNumber;
    }
}

solvePalindromeIntegers([123,323,421,121]);
solvePalindromeIntegers([32,2,232,1010]);


// 06. Password Validator;
function  solvePasswordValidator(inputPassword) {
    const validPasswordMessage = 'Password is valid';
    const notAllowedLengthMessage = 'Password must be between 6 and 10 characters';
    const notAllowedCharactersMessage = 'Password must consist only of letters and digits';
    const notEnoughDigitsMessage = 'Password must have at least 2 digits';


    const isAllowedLength =  isPasswordAllowedLength(inputPassword);
    const areAllCharactersAllowed = areAllCharactersAllowedInPassword(inputPassword);
    const areEnoughDigits = countDigitsInPassword(inputPassword) >= 2;

    function isPasswordAllowedLength(password) {
        return password.length >= 6 && password.length <= 10;
    }

    function areAllCharactersAllowedInPassword(password) {
        const pattern = /^[a-zA-Z0-9]+$/;

        return pattern.test(password);
    }

    function countDigitsInPassword(password) {
        let digitCounter = 0;

        for (let char of password) {
            if (!isNaN(parseInt(char, 10))) {
                digitCounter++;
            }
        }

        return digitCounter;
    }

    if (isAllowedLength && areAllCharactersAllowed && areEnoughDigits) {
        console.log(validPasswordMessage);
    } else {
        if (!isAllowedLength) {
            console.log(notAllowedLengthMessage);
        }
        if (!areAllCharactersAllowed) {
            console.log(notAllowedCharactersMessage);
        }
        if (!areEnoughDigits) {
            console.log(notEnoughDigitsMessage);
        }
    }
}

solvePasswordValidator('logIn');
solvePasswordValidator('MyPass123');
solvePasswordValidator('Pa$s$s');


// 07. NxN Matrix;
function solveSquareMatrix(size) {
    let matrix = [];

    for (let i = 0; i < size; i++) {
        let row = [];

        for (let j = 0; j < size; j++) {
            row.push(size);
        }

        matrix.push(row);
    }

    for (let i = 0; i < size; i++) {
        console.log(matrix[i].join(' '));
    }
}

solveSquareMatrix(3);
solveSquareMatrix(7);
solveSquareMatrix(2);


// 08. Perfect NUmber;
function solvePerfectNumber(number) {
    let isPerfect = false;
    let numberSum = 0;

    if (number > 0){
        for (let i = 1; i < number; i++) {
            if (number % i === 0) {
                numberSum += i;
            }
        }
    }

    if (numberSum === number && number > 0) {
            isPerfect = true;
        }

    if (isPerfect) {
        console.log('We have a perfect number!');
    } else {
        console.log('It\'s not so perfect.');
    }
}

solvePerfectNumber(6);
solvePerfectNumber(28);
solvePerfectNumber(1236498);


// 09. Loading Bar;
function solveLoadingBar(number) {
    const percent = `${number}%`;
    const loadedPercent = number / 10;

    let bar = '..........'.split('');
    let loadingBar;
    let statusMessage;

    let isComplete = false;

    if (loadedPercent === 10) {
        loadingBar = `${percent} [${calculateBar(loadedPercent)}]`;
        statusMessage = '100% Complete!'
        isComplete = true;
    } else {
        loadingBar = `${percent} [${calculateBar(loadedPercent)}]`;
        statusMessage = 'Still loading...';
    }

    function calculateBar(loadedPercent) {
        let newBar = bar.slice();
        for (let i = 0; i < loadedPercent; i++) {
            newBar[i] = '%';
        }

        bar = newBar.join('');

        return bar;
    }

    if (isComplete === true) {
        console.log(statusMessage);
        console.log(loadingBar);
    } else {
        console.log(loadingBar);
        console.log(statusMessage);
    }
}

solveLoadingBar(30);
solveLoadingBar(50);
solveLoadingBar(100);


// 10. Factorial Division;
function solveFactorialDivision(x, y) {
    let xFactorial = calculateFactorial(x);
    let yFactorial = calculateFactorial(y);


    function calculateFactorial(number) {
        let currentFactorial = 1;
        for (let i = 1; i <= number; i++) {
            currentFactorial *= i;
        }

        return currentFactorial;
    }

    const divisionResult = (xFactorial / yFactorial).toFixed(2);

    console.log(divisionResult);
}

solveFactorialDivision(5, 2);
solveFactorialDivision(6, 2);
