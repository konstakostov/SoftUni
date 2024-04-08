function solve(inputText, word) {
    let textArray = inputText.split(' ');
    let counter = 0;

    for (let i = 0; i < textArray.length; i++) {
        if (textArray[i] === word) {
            counter += 1;
        }
    }
    console.log(counter);
}

solve('This is a word and it also is a sentence', 'is');
solve('softuni is great place for learning new programming languages', 'softuni');