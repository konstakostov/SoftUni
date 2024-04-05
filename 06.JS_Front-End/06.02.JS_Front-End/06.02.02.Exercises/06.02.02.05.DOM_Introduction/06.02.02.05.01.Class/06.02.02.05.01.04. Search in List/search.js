function search() {
    const townListElements = document.getElementById('towns')
    const searchTextElement = document.getElementById('searchText').value;
    const resultElement = document.getElementById('result');

    let matchCount = 0

    const townElements = Array.from(townListElements.children)

    for (const townElement of townElements) {
        if (townElement.textContent.toLowerCase().includes(searchTextElement.toLowerCase())) {
            townElement.style.textDecoration = 'underline';
            townElement.style.fontWeight = 'bold';
            matchCount++;
        }
    }

    resultElement.textContent = `${matchCount} matches found`
}