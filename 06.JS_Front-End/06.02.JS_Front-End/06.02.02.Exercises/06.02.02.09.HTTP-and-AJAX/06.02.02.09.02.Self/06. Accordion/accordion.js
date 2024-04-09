function solution() {
    const baseURL = 'http://localhost:3030/jsonstore/advanced/articles/list';
    const articleURL = 'http://localhost:3030/jsonstore/advanced/articles/details/';

    const mainSection = document.getElementById('main');
    mainSection.innerHTML = '';

    async function loadPage() {
        const articlesList = await fetch(baseURL);
        const articles = await articlesList.json();

        for (const article of articles) {
            const divElement = document.createElement('div');
            divElement.className = 'accordion';

            divElement.innerHTML = `
                <div class="head">
                    <span>"${article['title']}"</span>
                    <button class="button" id="${article['_id']}">More</button>
                </div>
                <div class="extra">
                    <p>Scalable Vector Graphics .....</p>
                </div>
            `

            mainSection.appendChild(divElement);

            const buttonElement = divElement.querySelector('button');
            buttonElement.addEventListener('click', buttonElementFunctionality);

            async function buttonElementFunctionality() {
                const detailsOfArticle = await fetch(articleURL + article['_id']);
                const details = await detailsOfArticle.json();

                const pExtraElement = divElement.querySelector('.extra p');
                pExtraElement.textContent = details.content;

                if (buttonElement.textContent === 'More') {
                    pExtraElement.parentElement.style.display = 'block';
                    buttonElement.textContent = 'Less';
                } else if (buttonElement.textContent === 'Less') {
                    pExtraElement.parentElement.style.display = 'none';
                    buttonElement.textContent = 'More';
                }
            }
        }
    }

    loadPage();
}

solution()