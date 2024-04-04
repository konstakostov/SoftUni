// // Solution 01
// function calc() {
//     const inputNumber01 = document.getElementById('num1');
//     const inputNumber02 = document.getElementById('num2');
//     const numberSum = document.getElementById('sum');
//
//     const number01 = Number(inputNumber01.value);
//     const number02 = Number(inputNumber02.value);
//
//     numberSum.value = number01 + number02;
// }

// Solution 02
function calc() {
    const num01 = document.getElementById('num1').value;
    const num02 = document.getElementById('num2').value;

    const sum = Number(num01) + Number(num02);

    document.getElementById('sum').value = sum;
}
