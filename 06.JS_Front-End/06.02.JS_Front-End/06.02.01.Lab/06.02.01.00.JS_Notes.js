/*
Variables use camelCase;

Semicolon is used in the end of expressions;
Semicolon is NOT used at the end of statements;

In JS '' and "" are allowed; More commonly used are '', because usually in web project "" are used for the
HTML part of the code;
When using ' in string we can escape it by typing \'. That way JS reads ' as a character;

Primitive Data/Value Types:
- Boolean;
- null;
- undefined;
- Number;
- String;
- Symbol;
- BigInt;
The Primitive are saved in the stack;

Objects:
- Functions;
- Arrays;
Functions in JS are values;

let number = 10;    // Number;
let name = 'George';
let empty = null;
let unknown = undefined;
let isTrue = true;    // Boolean;
let person = {name: 'George;, age: 25}    // Object;
let array = [1, 2, 3];    // Array;

var - Uses function scope; Can be accessed anywhere in the function, including outside the initial block;
let and const– Uses block scope; When declared inside a block {} can NOT be accessed from outside the block;

let - Can be reassigned after initial assignment; Value can change; It is used when reassignment is necessary;
const - Cannot be reassigned after initial assignment, remains constant; Value remains fixed; It is used when
variable will not be reassigned;

Ternary Operator - Takes 3 statements; It is similar to if-else expressions;

Logical Operators:
! is NOT;
&& is AND;
|| is OR;


Truthy and Falsy Values:
Truthy - Value that coerces to true when evaluated in a boolean context;
Falsy - false, null, undefined, NaN, 0, 0n, "" considered falsy values;

 */


// Console print;
console.log('Hello, World!')


// Console print with string concatenation
const pi = 3.141592653
console.log('The number pi is: ' + pi + '!');


// Console print with string interpolation
console.log(`The number pi is ${pi}`);


// toFixed number output;
console.log(pi.toFixed(2))


// Rounding vs toFixed;
console.log(pi.toFixed(5))
console.log(Math.round(pi))

// Defining and Initialising Variables;
let a = 5;
let b = 10;

console.log(a + b);


// Conditional Statements
if (b <= 5) {
    console.log("b is lower or equal to 5");
} else if (b<= 10) {
    console.log("b is lower or equal to 10");
} else {
    console.log("b higher than 10");
}


// Function declaration;
function add(first, second) {
    console.log(first + second);
}

// Function invocation;
add(2, 3)


// Arithmetic Operations;
console.log(a + b);     // Additions;
console.log(a - b);     // Subtractions;
console.log(a * b);     // Multiplication;
console.log(a / b);     // Division;
console.log(a % b);     // Remainder;
console.log(a ** b);    // Exponential;


// Comparison Operations;
console.log(1 == '1');      //Equality; Returns True;
console.log(1 === '1');     //Identity; Returns False;
console.log(3 != '1');      //Inequality; Returns False;
console.log(3 !== '1');     //Strict Inequality; Returns True;
console.log(5 <= 5.5);      //Returns True;
console.log(5 <= 4);        //Returns False;
console.log(2 > 1.5);       //Returns True;
console.log(2 >= 2);        //Returns True;
console.log((5 > 7) ? 4 : 10)   //Ternary Operator; Returns 10;


// Switch Statement;
const name = 'pesho';
switch (name) {
    case 'gosho':
        console.log('Zrd gosho');
        break;
    case 'pesho':
        console.log('Maraba pesho');
        break;
    default:
        console.log("Koi si ti?")
        break;
}


// For Loop;
for (let i = 0; i < 5; i++) {
    console.log(i);
}


// While Loop;
let i = 4;
while ( i < 10) {
    i++;
    console.log(i);
}

