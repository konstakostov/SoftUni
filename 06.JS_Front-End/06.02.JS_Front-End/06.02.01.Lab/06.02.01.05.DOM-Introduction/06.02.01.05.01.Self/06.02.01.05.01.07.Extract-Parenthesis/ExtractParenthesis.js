function extract(content) {
    const textElement = document.getElementById(content);

    const pattern = /\((.*?)\)/g;
    const matches = textElement.textContent.match(pattern)
    let parenthesizedText = matches.map(match => match.slice(1, -1));

    return parenthesizedText.join('; ')
}