// 01. Array Rotation;
function solveArrayRotation(array, rotations) {
    let finalArray = array;

    for (let i = 0; i < rotations; i++) {
        const currentElement = finalArray.shift();

        finalArray.push(currentElement);
    }

    console.log(finalArray.join(' '));
}

solveArrayRotation([51, 47, 32, 61, 21], 2);
solveArrayRotation([32, 21, 61, 1], 4);
solveArrayRotation([2, 4, 15, 31], 5);


// 02. Print Every N-th Element from an Array;
function solvePrintElementsFromArray(array, step) {
    let resultArray = [];

    for (let i = 0; i < array.length; i += step) {
        const currentElement = array[i];

        resultArray.push(currentElement);
    }

    return resultArray;
}

solvePrintElementsFromArray(
    ['5',
    '20',
    '31',
    '4',
    '20'],
    2
);
solvePrintElementsFromArray(
    ['dsa',
    'asd',
    'test',
    'tset'],
    2
);
solvePrintElementsFromArray(
    ['1',
    '2',
    '3',
    '4',
    '5'],
    6
);


// 03. List of Names;
function solveListOfName(array) {
    array
        .sort((a, b) => {
            if (a.toLowerCase() > b.toLowerCase()) {
                return 1;
            } else if (a.toLowerCase() < b.toLowerCase()) {
                return -1;
            } else {
                return 0;
            }
        })
        .forEach((name, index) => console.log(`${index + 1}.${name}`));
}

solveListOfName(["John", "bob", "Christina", "Ema"]);


// 04. Sorting Numbers;
function solveSortingNumbers(array) {
    let arrayCopy = array.slice();
    arrayCopy.sort((a, b) => a - b);

    let finalArray = [];
    let index = 0;

    while (arrayCopy.length > 0) {
        let currentElement;

        if (index % 2 === 0) {
            currentElement = arrayCopy.shift();
        } else {
            currentElement = arrayCopy.pop();
        }

        finalArray.push(currentElement);

        index += 1
    }

    return finalArray;
}

solveSortingNumbers([1, 65, 3, 52, 48, 63, 31, -3, 18, 56]);


// 05. Reveal Words;
function solveRevealWords(strings, template) {
    let words = strings.split(', ');

    let startIndex = -1;
    let endIndex = -1;

    for (let i = 0; i < template.length; i++) {
        if (template[i] === '*') {
            if (startIndex < 0) {
                startIndex = i;
                endIndex = i + 1;
            } else {
                endIndex = i + 1;
            }
        } else {
            if (startIndex >= 0) {
                let wordLength = endIndex - startIndex;
                let word = words.find(w => w.length === wordLength);

                template = template.replace('*'.repeat(wordLength), word);

                startIndex = -1;
                endIndex = -1;
            }
        }
    }

    if (startIndex >= 0) {
        let wordLength = endIndex - startIndex;
        let word = words.find(w => w.length === wordLength);

        template = template.replace('*'.repeat(wordLength), word);
    }

    console.log(template)
}

solveRevealWords(
    'great',
    'softuni is ***** place for learning new programming languages'
);
solveRevealWords(
    'great, learning',
    'softuni is ***** place for ******** new programming languages'
);
solveRevealWords(
    'great, learning',
    'softuni is ***** place for ******** new programming languages *****'
);


// 06. Moder Times of #(HashTag);
function solveModernTimes(textAsString) {
    let textAsArray = textAsString.split(' ');
    const pattern = /^#[a-zA-Z]+$/;

    textAsArray.forEach(word => {
        if (pattern.test(word)) {
            let specialWord = word.substring(1);

            console.log(specialWord)
        }
    });
}

solveModernTimes('Nowadays everyone uses # to tag a #special word in #socialMedia');
solveModernTimes('The symbol # is known #variously in English-speaking #regions as the #number sign');


// 07. String Substring;
function solveStringSubstring(wordAsString, textAsString) {
    const mainStringLowerArray = textAsString.toLowerCase().split(' ');
    const searchStringDefault = wordAsString.toString();
    const searchStringLower = wordAsString.toLowerCase();


    if (mainStringLowerArray.includes(searchStringLower)) {
        console.log(searchStringDefault);
        return;
    } else {
        console.log(`${searchStringDefault} not found!`);
    }
}

solveStringSubstring('javascript','JavaScript is the best programming language');
solveStringSubstring('python', 'JavaScript is the best programming language');


// 08. Pascal-Case Splitter;
function solvePascalCaseSplitter(wordAsString) {
    const wordPattern = /[A-Z][a-z]*/g;

    const finalArray = wordAsString.match(wordPattern);

    console.log(finalArray.join(', '))
}

solvePascalCaseSplitter('SplitMeIfYouCanHaHaYouCantOrYouCan');
solvePascalCaseSplitter('HoldTheDoor');
solvePascalCaseSplitter('ThisIsSoAnnoyingToDo');
