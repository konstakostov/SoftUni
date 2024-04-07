function create(words) {
    const contentElement = document.getElementById('content');

    // Create div with paragraph;
    const divElements = words
        .map(word => {
            // Create paragraph & Add text content & Hiding paragraph;
            const pElement = document.createElement('p');
            pElement.textContent = word;
            pElement.style.display = 'none';

            // Create div & Append paragraph to div;
            const divElement = document.createElement('div');
            divElement.appendChild(pElement);

            // Return div;
            return divElement;
        })

    // Show paragraph on dib click;
    divElements
        .forEach(divElement => {
            divElement.addEventListener('click', () => {
                const pElement = divElement.querySelector('p');
                pElement.style.display = 'block';
            })
        })

    // Append elements to div#content;
    divElements.forEach(divElement => contentElement.appendChild(divElement));  // <-- Not Efficient;
    // contentElement.append(...divElements); <-- Does Not Work in Judge;

    // Recommended way for optimizing efficiency;
    const divElementsFragments = document.createDocumentFragment();
    divElements.forEach(divElement => divElementsFragments.appendChild(divElement));
}
