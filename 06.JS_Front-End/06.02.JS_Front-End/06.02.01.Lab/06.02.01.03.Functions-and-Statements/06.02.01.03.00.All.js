/*
Functions can be declared like:
- Function declaration;
- Function expression; It is also known as anonymous function;
- Arrow function;

First class functions are treated like any other variables; They are passed as an argument; They can be returned by
another function; They can be assigned as value to a variable; 'These types of functions can go anywhere that any other
value can go - there are few to no restrictions';

Arrow functions have shorthand syntax to be declared; They operate in the context of their enclosing scope;
*/


// Function declaration;
function printSomeText01() {
    console.log('Some text 01');
}

// Function expression;
let printSomeText02 = function () {
    console.log('Some text 02');
}

// Arrow function;
const printSomeText03 = () => console.log('Some text 03');

// Function invocation;
printSomeText01();  // Declaration;
printSomeText02();  // FExpression;
printSomeText03();  // Arrow;


// Invoke function from another function;
function masterPrintSomeText() {
    console.log('Master Function will print the following text:')
    printSomeText01();
    printSomeText02();
    printSomeText03();
}

masterPrintSomeText();


// // First-Class Functions;
// Pass function as an argument;
function executeOperation(operation, operandA, operandB) {
    const result = operation(operandA, operandB);

    console.log(`The result of this operations is equal to ${result.toFixed(2)}`);
}

function operationAdd(a, b) {
    return a + b;
}

const operationSubtract = function (a, b) {
    return a - b;
}

// Pass function by reference;
executeOperation(operationAdd, 1, 2);
executeOperation(operationSubtract, 1, 2);

// Pass function expression body as argument;
executeOperation(function (a, b) {
    return a / b
}, 10, 2);

// Pass arrow function body as argument;
executeOperation((a, b) => a * b, 2, 5);


// // Arrow functions;
// Arrow function statement body;
const solveSumNumbers01 = (a, b) => {
    const resultSum = a + b;

    return resultSum;
}

console.log(solveSumNumbers01(1, 2));

// Arrow function expression body;
const solveSumNumbers02 = (a, b) => a + b;

console.log(solveSumNumbers02(2, 2));

// Expression body arrow function with single parameter;
const double = a => a * 2;

console.log(double(3));


// 01. Format Grade;
function solveFormatGrade(grade) {
    const result = formatGrade(grade);

    console.log(result);
    function formatGrade(grade) {
        let formattedGrade = '';

        if (grade < 3.00) {
            formattedGrade = `Fail (2)`;
        } else if (grade >= 3.00 && grade < 3.50) {
            formattedGrade = `Poor (${grade.toFixed(2)})`;
        } else if (grade >= 3.50 && grade < 4.50) {
            formattedGrade = `Good (${grade.toFixed(2)})`;
        } else if (grade >= 4.50 && grade < 5.50) {
            formattedGrade = `Very good (${grade.toFixed(2)})`;
        } else if (grade >= 5.50) {
            formattedGrade = `Excellent (${grade.toFixed(2)})`;
        }

        return formattedGrade;
    }
}

solveFormatGrade(3.33);
solveFormatGrade(4.50);
solveFormatGrade(2.99);


// 02. Math Power;
function solveMathPower(number, power) {
    console.log(`${Math.pow(number, power)}`);
}

solveMathPower(2, 8);
solveMathPower(3, 4);


// 03. Repeat String;
function solveRepeatString(text, count) {
    return text.repeat(count)
}

console.log(solveRepeatString("abc", 3));
console.log(solveRepeatString("String", 2));


// 04. Orders;
function solveOrders(product, quantity) {
    const productPrice = getProductPrice(product);

    let totalPrice = productPrice * quantity;

    console.log(totalPrice.toFixed(2));

    function getProductPrice(product) {
        switch (product) {
            case 'coffee':
                return 1.50;
            case 'water':
                return 1.00;
            case 'coke':
                return 1.40;
            case 'snacks':
                return 2;
        }
    }
}

solveOrders("water", 5);
solveOrders("coffee", 2);


// 05. Simple Calculator;
function solveSimpleCalculator(a, b, operator) {
    const operation = determineOperation(operator);

    const result = operation(a, b);

    console.log(result)

    function determineOperation(operator) {
        switch (operator) {
            case 'multiply':
                return (a, b) => a * b;
            case 'divide':
                return (a, b) => a / b;
            case 'add':
                return (a, b) => a + b;
            case 'subtract':
                return (a, b) => a - b;
        }
    }
}

solveSimpleCalculator(5, 5, 'multiply');
solveSimpleCalculator(40,8,'divide');
solveSimpleCalculator(12,19,'add');
solveSimpleCalculator(50, 13, 'subtract' );


// 06. Sign Check;
function solveSignCheck(a, b, c) {
    let negativeCounter = 0;
    let signStatus = '';

    numberCheck(a);
    numberCheck(b);
    numberCheck(c);

    signCheck(negativeCounter);

    console.log(signStatus)

    function numberCheck(num) {
        if (num < 0) {
            negativeCounter += 1;
        }
    }

    function signCheck(negativeSignsSum) {
        if (negativeSignsSum % 2 === 0) {
        signStatus = 'Positive';
    } else {
        signStatus = 'Negative';
    }
    }
}

solveSignCheck( 5,  12, -15);
solveSignCheck(-6, -12,  14);
solveSignCheck(-1, -2, -3);
solveSignCheck(-5,  1,  1);
