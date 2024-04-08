function addItem() {
    const inputTextElement = document.getElementById('newItemText');
    const listItemElements = document.getElementById('items');

    let newListItem = document.createElement('li');
    newListItem.textContent = inputTextElement.value;

    listItemElements.appendChild(newListItem);

    inputTextElement.value = '';
}