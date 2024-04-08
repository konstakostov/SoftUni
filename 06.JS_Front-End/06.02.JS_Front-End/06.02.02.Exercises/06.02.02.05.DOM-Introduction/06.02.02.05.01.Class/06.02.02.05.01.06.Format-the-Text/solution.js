function solve() {
    const textAreaElement = document.getElementById('input');
    const outputElement = document.getElementById('output');

    const text = textAreaElement.value;

    result = text
        .split('.')
        .filter(sentence => !!sentence)
        .reduce((result, sentence, i) => {
            const resultIndex = Math.floor(i / 3);

            if (!result[resultIndex]) {
                result[resultIndex] = []
            }

            result[resultIndex].push(sentence.trim());

            return result;
        }, [])
        .map(sentences => `<p>${sentences.join('. ')}.</p>`)    // Without '.' before </p> there isn't 100/100;
        .join('\n');

    outputElement.innerHTML = result;
}