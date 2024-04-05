function solve() {
    const textElement = document.getElementById('text');
    const conventionElement = document.getElementById('naming-convention');
    const resultElement = document.getElementById('result');

    const text = textElement.value;
    const convention = conventionElement.value;

    const convertToPascalCase = (text)  => {
            return text
                .split(' ')
                .map(word => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase())
                .join('');
        }

    const convertor = {
        'Pascal Case': convertToPascalCase,
        'Camel Case': (text) =>
            convertToPascalCase(text).charAt(0).toLowerCase() + convertToPascalCase(text).slice(1),
    }

    if (convertor[convention]) {
        resultElement.textContent = convertor[convention](text);
    } else {
        resultElement.textContent = 'Error!';
    }
}