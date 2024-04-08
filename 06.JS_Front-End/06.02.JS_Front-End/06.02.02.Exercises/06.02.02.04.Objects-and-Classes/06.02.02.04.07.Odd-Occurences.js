function solve(inputText) {
    const words = inputText.toLowerCase().split(' ')

    let occurrences = {};

    for (const word of words) {
        if (word in occurrences) {
            occurrences[word] += 1;
        } else {
            occurrences[word] = 1
        }
    }

    const oddOccurrences = Object
        .keys(occurrences)
        .filter(word => occurrences[word] % 2 !== 0);


    console.log(oddOccurrences.join(' '));
}

solve('Java C# Php PHP Java PhP 3 C# 3 1 5 C#');
solve('Cake IS SWEET is Soft CAKE sweet Food');