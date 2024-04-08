function solve(inputArray) {
    const words = inputArray.shift().split(' ');
    let tracker = {};


    for (const word of words) {
        let counter = 0;

        for (const currentWord of inputArray) {
            if (word === currentWord) {
                counter += 1
            }
        }

        tracker[word] = counter
    }

    Object
        .entries(tracker)
        .sort((a, b) => b[1] - a[1])
        .forEach(([word, count]) => console.log(`${word} - ${count}`))
}

solve(
    [
        'this sentence',
        'In', 'this', 'sentence', 'you', 'have', 'to', 'count', 'the', 'occurrences', 'of', 'the', 'words', 'this', 'and', 'sentence', 'because', 'this', 'is', 'your', 'task'
    ]
);
solve(
    [
        'is the',
        'first', 'sentence', 'Here', 'is', 'another', 'the', 'And', 'finally', 'the', 'the', 'sentence'
    ]
);