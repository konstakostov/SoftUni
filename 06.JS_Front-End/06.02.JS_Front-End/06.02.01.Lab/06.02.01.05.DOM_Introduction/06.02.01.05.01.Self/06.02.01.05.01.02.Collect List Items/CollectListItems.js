function extractText() {
    const listItemElements = document.querySelectorAll('ul#items li');
    const textAreaElement = document.getElementById('result');

    for (const listItem of listItemElements) {
        textAreaElement.textContent += listItem.textContent + '\n';
    }
}