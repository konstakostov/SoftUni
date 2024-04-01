function solve(inputString, inputText) {
    const inputWords = inputString.split(', ');
    let finalText = inputText.split(' ');

    inputWords.forEach(searchedWord => {
        finalText = finalText.map(word => {
            if (word.length === searchedWord.length && word.includes('*')) {
                return searchedWord;
            } else {
                return word;
            }
        });
    });

    console.log(finalText.join(' '));
}

solve(
    'great',
    'softuni is ***** place for learning new programming languages'
);
solve(
    'great, learning',
    'softuni is ***** place for ******** new programming languages'
);

