function subtract() {
    const firstNumberElement = document.getElementById('firstNumber').value;
    const secondNumberElement = document.getElementById('secondNumber').value;
    const resultElement = document.getElementById('result');

    resultElement.textContent = Number(firstNumberElement) - Number(secondNumberElement);
}