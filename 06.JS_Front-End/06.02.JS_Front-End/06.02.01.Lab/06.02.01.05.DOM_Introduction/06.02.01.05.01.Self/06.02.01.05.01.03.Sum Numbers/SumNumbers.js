function calc() {
    const firstNumberElement = document.getElementById('num1');
    const secondNumberElement = document.getElementById('num2');
    const sumNumbersElement = document.getElementById('sum');

    sumNumbersElement.value = Number(firstNumberElement.value) + Number(secondNumberElement.value);
}
