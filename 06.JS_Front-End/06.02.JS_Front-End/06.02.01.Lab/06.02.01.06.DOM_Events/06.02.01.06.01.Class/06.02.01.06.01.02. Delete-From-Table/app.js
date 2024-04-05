function deleteByEmail() {
    const trElements = document.querySelectorAll('#customers tbody tr')
    const inputEmailElement = document.querySelector('input[name=email]')
    const resultElement = document.getElementById('result')

    const trElementToFind = Array
        .from(trElements)
        .find(element => element.children[1].textContent.includes(inputEmailElement.value))

    if (trElementToFind) {
        trElementToFind.remove();
        resultElement.textContent = 'Deleted.';
    } else {
        resultElement.textContent = 'Not found.';
    }
    inputEmailElement.value = '';
}