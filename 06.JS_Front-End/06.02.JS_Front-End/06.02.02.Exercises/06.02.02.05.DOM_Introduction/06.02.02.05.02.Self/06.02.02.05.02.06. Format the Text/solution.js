function solve() {
    const inputText = document.getElementById('input').value;
    const outputElement = document.getElementById('output');

    const inputTextList = inputText
        .split('.')
        .filter(sentence => sentence.trim().length > 0);

    let result = '';
    let paragraph = [];


    for (let i = 0; i < inputTextList.length; i++) {
        paragraph.push(inputTextList[i].trim());

        if ((i + 1) % 3 === 0 || i === inputTextList.length - 1) {
            result += `<p>${paragraph.join('. ')}.</p>\n`;
            paragraph = []
        }
    }

    outputElement.innerHTML = result.slice(0, result.length - 1);
}