function solve(inputText, inputWord) {
    let outputText = inputText;
    const censorWord = '*'.repeat(inputWord.length);

    while (outputText.includes(inputWord)) {
        outputText = outputText.replace(inputWord, censorWord);
    }

    console.log(outputText);
}

solve('A small sentence with some words', 'small');
solve('Find the hidden word', 'hidden');
