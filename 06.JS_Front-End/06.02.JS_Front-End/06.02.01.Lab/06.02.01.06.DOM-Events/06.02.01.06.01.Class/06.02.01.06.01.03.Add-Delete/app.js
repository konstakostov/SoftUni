function addItem() {
    const inputItemElement = document.getElementById('newItemText');
    const itemListElement = document.getElementById('items');

    // Create new item element;
    const newInputItemElement = document.createElement('li');
    newInputItemElement.textContent = inputItemElement.value;

    // Create new link element;
    const deleteLinkElement = document.createElement('a');
    deleteLinkElement.textContent = '[Delete]';
    deleteLinkElement.href = '#';

    // Add event to the link element;
    deleteLinkElement.addEventListener('click', () => {
        newInputItemElement.remove();
    })

    // Append the link element to newInputItemElement;
    newInputItemElement.appendChild(deleteLinkElement);

    // Append the new element to itemListElement;
    itemListElement.appendChild(newInputItemElement);

    //Clear the input;
    inputItemElement.value = '';
}