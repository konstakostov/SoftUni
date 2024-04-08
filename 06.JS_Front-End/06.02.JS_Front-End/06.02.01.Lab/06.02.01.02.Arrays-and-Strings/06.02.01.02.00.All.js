/*
Arrays are list-like objects;

Arrays are reference type; The variable points to an address in the memory;

Arrays are created using n array literal:

Arrays length or types are NOT fixed;

JS arrays are sparse;

Destructuring Syntax:
- Allows declaring multiple values on a single line;
- Expression that unpacks values from arrays or objects, into distinct variables;
- rest operator: ...example; Think of *arg in Python;
- The rest operator can also be used to collect function parameters into an array;

For-of Loop:
- Iterates through all elements in a collection;
- Cannot access the current index;
*/


// Declaring an empty array;
let empty = [];     // truthy value
console.log(empty);

// Declaring an array;
let numbers = [10, 20, 30, 40, 50];
let names = ['Stoya,', 'Pesho', 'Ivan'];

console.log(numbers);
console.log(names);


// Change array by reference;
numbers[0] = 11;

console.log(numbers);

// Dynamically add elements to an array;
empty[0] = 0;
empty[1] = 1;

console.log(empty);


// Get array length;
console.log(numbers.length);


// Access array element;
console.log(numbers[numbers.length - 1]);
console.log(numbers[1]);

// Array destructuring assignment;
let [firstNumber, secondNumber, thirdNumber, ...restNumbers] = [1, 2 ,3, 4, 5, 6, 7, 8]
console.log(firstNumber);
console.log(secondNumber);
console.log(thirdNumber);
console.log(restNumbers);


// For-of Loop;
for (let num in numbers) {
    console.log(num);
}


// Array Hack 01
names[10] = 'Stamat';
console.log(names.length);
console.log(names);


// Array Hack 02
let arr = [1, 2, 3]
console.log(arr.length);

arr.length = 10;
console.log(arr);

arr.length = 2;
console.log(arr);


/*
Arrays methods:
- pop method: Get and remove last item; Same in Python;
- push method: Add last item; In python is append;
- shift method: Removes first item; In python is dequeue;
- unshift method: Add first item; In python is queue;
- splice method: Changes content of an array by removing/replacing existing element and/or adding new elements;
- reverse method; Reverses the element in the array;
- join method; Concatenates all elements in an array and returns them as a string; Same as in python;
- slice method: Takes a part of the array, without removing the elements from it; Can be used to create a shallow copy
of the array and is stored in separate part of the memory;
- include method: Check if element exists in array; Allows checking if it exists from specific index onward;
- indexOf method: Finds the index of an element; It returns the index of the first found element if there are multiple
elements; If the element does not exist it returns -1;
- find method: Find specific element in an array; Accepts function as argument;
- forEach method: Executes a provide function once for each element of the array; Accepts function as argument;
- map method: Creates a new array with results of calling a provided function on every element in the calling array;
- filter method: Filters elements from an array; Accepts function as argument;
*/


// Get and remove last item;
let cars = ['BMW', 'Audi', 'Mercedes', 'Toyota', 'Honda'];
console.log(cars);

let lastCar = cars.pop();
console.log(lastCar);
console.log(cars);


// Add last item;
let newLength = cars.push('Peugeot', 'Opel', 'VW');
console.log(newLength);
console.log(cars);


// Remove first element;
let firstCar = cars.shift()

console.log(firstCar);
console.log(cars);


// Add first element;
let newUnsiftedLength = cars.unshift('BMW')

console.log(newUnsiftedLength);
console.log(cars);


// Remove item with splice;
let deletedCars = cars.splice(2, 2);

console.log(deletedCars);
console.log(cars);


// Add item with splice;
let addCars = cars.splice(2, 0, 'Toyota');

console.log(addCars);
console.log(cars);


// Add and remove item with splice;
let addDeleteCars = cars.splice(0, 2, 'Lada', 'Lamborghini');

console.log(addDeleteCars);
console.log(cars);


// Reverse array;
let reversedCars = cars.reverse();

console.log(reversedCars);
console.log(cars);


// Join method;
let joinedCars = cars.join(', ');

console.log(joinedCars);
console.log(cars);


// Slice start;
let startCars = cars.slice(0, 3);

console.log(startCars);
console.log(cars);


// Shallow copy with slice method;
let shallowCars = cars.slice();

console.log(shallowCars);
console.log(cars);


// Slice from middle to end;
let middleEndCars = cars.slice(3, 3);

console.log(middleEndCars);
console.log(cars);


// Check if element exists in array;
let isToyotaIncluded = cars.includes('Toyota');
let isBugattiIncluded = cars.includes('Bugatti');

console.log(isToyotaIncluded);
console.log(isBugattiIncluded);


// Find index of element;
let toyotaIndex = cars.indexOf('Toyota');

console.log(toyotaIndex);


// Find specific element;
let toyotaElement = cars.find(car => car === 'Toyota');

console.log(toyotaElement);


// Find all indices of all elements, sharing the same value
let topCars = ['Toyota', 'BMW', 'Toyota', 'Audio', 'Toyota'];

let tIndex = topCars.indexOf('Toyota');
while (tIndex >= 0) {
    console.log(tIndex);

    tIndex = topCars.indexOf('Toyota', tIndex + 1);
}


// forEach;
cars.forEach(car => console.log(car));


// Map;
let initialNumbers = [1, 2, 3, 4, 5];
let doubleNumbers = initialNumbers.map(number => number * 2);

console.log(initialNumbers);
console.log(doubleNumbers);


// Filter;
let oddNumbers = initialNumbers.filter(number => number % 2 !== 0);
let evenNumbers = initialNumbers.filter(number => number % 2 === 0);

console.log(oddNumbers);
console.log(evenNumbers);


// Reduce; (Not part of the learning schedule. Check out later if needed.);
let sumInitialNumbers = initialNumbers.reduce((sum, number) => sum + number, 0 );

console.log(sumInitialNumbers);


// Chaining;
let doubleOddNumbers = initialNumbers
    .filter(number => number % 2 !== 0)
    .map(number => number * 2);

console.log(doubleOddNumbers);


/*
Strings are immutables (they can't be changed);

String Methods:
- concat method: Concatenates 2 or more strings; Equivalent to using '+' to concatenate strings;
- indexOf(subst): Checking if a substring is in the string; It is case-sensitive; Finds first occurrence and returns
result; Returns index;
- lastIndexOf(subst): Checking if a substring is in the string; It is case-sensitive; Finds last occurrence and returns
result; Returns index;
- substring(startIndex, endIndex): Extracts substring from the given index range;
- replace(searchWord, replacementWord): It finds the first existing match in the string and replaces it with the
provided replacement string;
- replaceAll(searchWord, replacementWord): It finds all existing matches in the string and replaces them with the
provided replacement string;
- split(separator): Converts string into array;
- includes(subst): Checks if the substring is in the string;
- repeat(count): Repeats a string;
- trim(): Removes whitespaces from both ends of the string;
- trimStart(): Removes whitespaces from the beginning of the  string;
- trimEnd(): Removes whitespaces from the end of the string;
- startsWith(substr): Checks if string string starts with the provided substring;
- endsWith(substr):Checks if string string ends with the provided substring;
- padStart(length, substr): Add substring to the start of a string, until the provided length is reached;
- padEnd(length, substr): Add substring to the end of a string, until the provided length is reached;
*/


// String Concatenating;
let firstName = 'Ivan';
let lastName = 'Ivanov';

let fullName = firstName + ' ' + lastName;

let greetings = 'Hi, ';
let firstSentence = greetings.concat(fullName) + '! ';

let secondSentence = 'How are you today?';
let finalText = firstSentence.concat(secondSentence);

console.log(finalText);


// indexOf and lastIndexOf;
let randomText = 'I am JavaScript developer not a Java developer.';
let indexOfJava = randomText.indexOf('Java');
let lastIndexOfJava = randomText.lastIndexOf('Java');

console.log(indexOfJava);
console.log(lastIndexOfJava);


// Substring;
let theBestLanguage = randomText.substring(0, 10);

console.log(theBestLanguage);


// replace and replaceAll;
let replaceRandomText = randomText.replace('Java', 'Type');
let replaceAllRandomText = randomText.replaceAll('Java', 'Fake');

console.log(replaceRandomText);
console.log(replaceAllRandomText);


// Split;
let allRandomTextWords = randomText.split(' ');

console.log(allRandomTextWords);


// Includes;
let includeJava = randomText.includes('Java');
let includePython = randomText.includes('Python');

console.log(includeJava);
console.log(includePython);


// Repeat;
let trollText = 'Tro ' + 'lo '.repeat(10);

console.log(trollText);


// trim, trimStart and trimEnd;
let whiteSpaceString = '    Blank    ';

console.log(whiteSpaceString.trim());
console.log(whiteSpaceString.trimStart());
console.log(whiteSpaceString.trimEnd());


// startsWith and endWith;
let exampleSentence = 'I am an Engineer and Python Developer';

console.log(exampleSentence.startsWith('I am'));
console.log(exampleSentence.startsWith('am'));

console.log(exampleSentence.endsWith('Python Developer'));
console.log(exampleSentence.endsWith('Python'));


// padStart and PadEnd;
let randomNumberString = '101';

console.log(randomNumberString.padStart(10, '305'));
console.log(randomNumberString.padEnd(10, '305'));


/*
RegEx in JS can be constructed in 2 ways:
- Regular Expression Literal; The literal is: '/' at the start and end of the expression'
- Constructor Function RegExp;
*/


let exampleString = 'I am a Python developer, Python is awesome!';


// RegEx literal;
let literalPattern = /Python/ig;


// RegEx function constructor;
let constructorPattern = new RegExp('Python', 'ig');


// Test RegEx pattern;
console.log(literalPattern.test(exampleString));
console.log(constructorPattern.test(exampleString));


// Match by pattern (Exec RegEx pattern);
console.log(literalPattern.exec(exampleString));
console.log(literalPattern.exec(exampleString));
console.log(literalPattern.exec(exampleString));

console.log(constructorPattern.exec(exampleString));
console.log(constructorPattern.exec(exampleString));
console.log(constructorPattern.exec(exampleString));


// String RegEx pattern;
console.log(exampleString.match(literalPattern));
console.log(exampleString.match(constructorPattern));


console.log(exampleString.matchAll(literalPattern));

const literalMatch = exampleString.matchAll(literalPattern);

for (const match of literalMatch) {
    console.log(match)
}

console.log(exampleString.matchAll(constructorPattern));

const constructorMatch = exampleString.matchAll(literalPattern);

for (const match of constructorMatch) {
    console.log(match)
}


// 01. Sum First and Last Array Elements;
function solveFirstLastArraySum(array) {
    let firstNumber = array[0];
    let lastNumber = array[array.length - 1];

    let sumFirstLastElement = firstNumber + lastNumber;

    console.log(sumFirstLastElement);
}

solveFirstLastArraySum([20, 30, 40]);
solveFirstLastArraySum([10, 17, 22, 33]);
solveFirstLastArraySum([11, 58, 69]);


// 02. Reverse an Array of Numbers;
function reverseNumbersArray01(number, array) {
    let newArray = [];

    for (let i = 0; i < number; i++) {
        newArray.push(array[i]);
    }

    let newArrayReversed = newArray.reverse();

    console.log(newArrayReversed.join(' '));
}

reverseNumbersArray01(3, [10, 20, 30, 40, 50]);
reverseNumbersArray01(4, [-1, 20, 99, 5]);
reverseNumbersArray01(2, [66, 43, 75, 89, 47]);


function reverseNumbersArray02(number, array) {
    let newArray = array.slice(0, number);

    let newArrayReversed = newArray.reverse();

    console.log(newArrayReversed.join(' '));
}

reverseNumbersArray02(3, [10, 20, 30, 40, 50]);
reverseNumbersArray02(4, [-1, 20, 99, 5]);
reverseNumbersArray02(2, [66, 43, 75, 89, 47]);


// 03. Even and Odd Subtraction;
function solveEvenOddSubtraction(array) {
    let oddSum = 0;
    let evenSum = 0;

    for (let i = 0; i < array.length; i++) {
        let currentNumber = Number(array[i])

        if (currentNumber % 2 === 0) {
            evenSum += currentNumber;
        } else {
            oddSum += currentNumber;
        }
    }

    const sumDifference = evenSum - oddSum;

    console.log(sumDifference);
}

solveEvenOddSubtraction([1,2,3,4,5,6]);
solveEvenOddSubtraction([3,5,7,9]);
solveEvenOddSubtraction([2,4,6,8,10]);

// 04. Substring;
function solveSubstring(string, startIndex, endIndex) {
    let finalString = string.substring(startIndex, startIndex + endIndex);

    console.log(finalString);
}

solveSubstring('ASentence', 1, 8);
solveSubstring('SkipWord', 4, 7);


// 05. Censored Words;
function solveCensoredWords(text, uncensoredWord) {
    let outputText = text
    let censoredWord = '*'.repeat(uncensoredWord.length)

    while (outputText.includes(uncensoredWord)) {
        outputText = outputText.replace(uncensoredWord, censoredWord);
    }

    console.log(outputText);
}

solveCensoredWords('A small sentence with some words', 'small');
solveCensoredWords('Find the hidden word', 'hidden');


// 06. Count String Occurrences;
function solveStringOccurences(textAsString, word) {
    const textAsArray = textAsString.split(/\s+/);
    let wordCounter = 0;

    for (let i = 0; i < textAsArray.length; i++) {
        if (textAsArray[i] === word) {
            wordCounter += 1;
        }
    }

    console.log(wordCounter);
}

solveStringOccurences('This is a word and it also is a sentence', 'is');
solveStringOccurences('softuni is great place for learning new programming languages', 'softuni' );
