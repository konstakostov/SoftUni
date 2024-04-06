function deleteByEmail() {
    const rowElements = document.querySelectorAll('tbody tr');
    const inputEmailElement = document.querySelector('input[name=email]')
    const resultElement = document.getElementById('result')

    const rowToFind = Array
        .from(rowElements)
        .find(cell => cell.children[1].textContent.includes(inputEmailElement.value));

    if (rowToFind) {
        rowToFind.remove();
        resultElement.textContent = 'Deleted.';
    } else {
        resultElement.textContent = 'Not found.';
    }

    inputEmailElement.value = '';
}