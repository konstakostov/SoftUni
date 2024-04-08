function addItem() {
    const listElement = document.getElementById('items');
    const inputElement = document.getElementById('newItemText');


    const liElement = document.createElement('li');
    liElement.textContent = inputElement.value;

    const linkDeleteElement = document.createElement('a');
    linkDeleteElement.textContent = '[Delete]';
    linkDeleteElement.href = '#';

    linkDeleteElement.addEventListener('click', () => {
        liElement.remove();
    })

    liElement.appendChild(linkDeleteElement);
    listElement.appendChild(liElement);

    inputElement.value = '';
}