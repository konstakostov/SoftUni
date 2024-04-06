function search() {
    const listItemElements = document.getElementById('towns');
    const searchedElement = document.getElementById('searchText');
    const resultElement = document.getElementById('result');

    let matchesFound = 0;

    const foundTowns = Array.from(listItemElements.children)

    for (const town of foundTowns) {
        if (town.textContent.toLowerCase().includes(searchedElement.value.toLowerCase())) {
            town.style.textDecoration = 'underline';
            town.style.fontWeight = 'bold';

            matchesFound +=1;
        } else {
            town.style.textDecoration = 'none';
            town.style.fontWeight = 'normal';
        }
    }

    resultElement.textContent = `${matchesFound} matches found`;
}