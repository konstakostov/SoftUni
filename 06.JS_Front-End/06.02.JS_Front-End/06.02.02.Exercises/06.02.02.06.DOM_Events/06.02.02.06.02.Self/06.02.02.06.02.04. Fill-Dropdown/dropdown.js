function addItem() {
    const textInputElement = document.getElementById('newItemText');
    const valueInputElement = document.getElementById('newItemValue');
    const selectElement = document.getElementById('menu');

    const textValue = textInputElement.value;
    const valueValue = valueInputElement.value;

    const newOptionElement = document.createElement('option');
    newOptionElement.textContent = textValue;
    newOptionElement.value = valueValue;

    selectElement.appendChild(newOptionElement);

    textInputElement.value = '';
    valueInputElement.value = '';
}