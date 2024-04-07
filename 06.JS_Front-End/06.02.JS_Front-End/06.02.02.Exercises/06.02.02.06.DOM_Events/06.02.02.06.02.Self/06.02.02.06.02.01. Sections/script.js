function create(words) {
    const divElements = document.getElementById('content');

    for (const word of words) {
        const pNewElement = document.createElement('p');
        pNewElement.textContent = word;
        pNewElement.style.display = 'none';

        const divNewElement = document.createElement('div');
        divNewElement.style.display = 'block';

        divNewElement.addEventListener('click', () => {
            pNewElement.style.display = '';
        })

        divNewElement.appendChild(pNewElement)

        divElements.appendChild(divNewElement)
    }
}
