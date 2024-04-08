function solve(inputWord, inputText) {
    const word = inputWord.toLowerCase()
    const textArray = inputText.toLowerCase().split(' ');
    let wordFound = false;

    for (const currentWord of textArray) {
        if (currentWord === word) {
            wordFound = true;
            break;
        }
    }

    if (wordFound) {
        console.log(word);
    } else {
        console.log(`${word} not found!`)
    }
}

solve('javascript','JavaScript is the best programming language');
solve('python', 'JavaScript is the best programming language');