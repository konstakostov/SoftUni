function solve() {
    const inputNumberElement = document.getElementById('input');
    const selectMenuToElement = document.getElementById('selectMenuTo');
    const resultElement = document.getElementById('result')
    const convertButtonElement = document.querySelector('button');

    const binaryOptionalElement = selectMenuToElement.querySelector('option');
    binaryOptionalElement.value = 'binary';
    binaryOptionalElement.textContent = 'Binary';

    const hexadecimalOptionalElement = document.createElement('option');
    hexadecimalOptionalElement.value = 'hexadecimal';
    hexadecimalOptionalElement.textContent = 'Hexadecimal';
    selectMenuToElement.appendChild(hexadecimalOptionalElement);

    const convertors = {
        binary: convertDecimalToBinary,
        hexadecimal: convertDecimalToHexadecimal,
    };

    convertButtonElement.addEventListener('click', () => {
        const numberValue = Number(inputNumberElement.value)

        resultElement.value = convertors[selectMenuToElement.value](numberValue);
    });

    function convertDecimalToBinary(number) {
        return number.toString(2).toUpperCase();
    }

    function convertDecimalToHexadecimal(number) {
        return number.toString(16).toUpperCase();
    }
}