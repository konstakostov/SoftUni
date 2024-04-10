window.addEventListener("load", solve);

function solve() {
    const expensesTypeInput = document.getElementById('expense');
    const amountInput = document.getElementById('amount');
    const dateInput = document.getElementById('date');

    const addButton = document.getElementById('add-btn');
    addButton.addEventListener('click', addButtonFunctionality);

    const deleteButton = document.querySelector('#expenses .delete');
    deleteButton.addEventListener('click', deleteButtonFunctionality);

    const previewList = document.getElementById('preview-list');
    const expensesList = document.getElementById('expenses-list');

    function addButtonFunctionality() {
        const expensesType = expensesTypeInput.value;
        const amount = amountInput.value;
        const date = dateInput.value;

        if (expensesType !== '' && amount !== '' && date !== '') {
            // Create p elements & set textContent;
            const pTypeElement = document.createElement('p');
            pTypeElement.textContent = `Type: ${expensesType}`

            const pAmountElement = document.createElement('p');
            pAmountElement.textContent = `Amount: ${amount}$`

            const pDateElement = document.createElement('p');
            pDateElement.textContent = `Date: ${date}`

            // Create article element & set append p elements;
            const articleElement = document.createElement('article');
            articleElement.appendChild(pTypeElement);
            articleElement.appendChild(pAmountElement);
            articleElement.appendChild(pDateElement);

            // Create button elements & set class name & set textContent & addEventListener;
            const buttonEditElement = document.createElement('button');
            buttonEditElement.className = 'btn edit';
            buttonEditElement.textContent = 'edit';
            buttonEditElement.addEventListener('click', buttonEditElementFunctionality)

            const buttonOkElement = document.createElement('button');
            buttonOkElement.className = 'btn ok';
            buttonOkElement.textContent = 'ok';
            buttonOkElement.addEventListener('click', buttonOkElementFunctionality)

            // Create div element & set class name & append button elements;
            const divElement = document.createElement('div');
            divElement.className = 'buttons';
            divElement.appendChild(buttonEditElement);
            divElement.appendChild(buttonOkElement);

            // Create li element & set class name & append article element and div element;
            const liElement = document.createElement('li');
            liElement.className = 'expense-item';
            liElement.appendChild(articleElement);
            liElement.appendChild(divElement);

            // Append li item to the ul element, with class 'preview-list';
            previewList.appendChild(liElement);

            // Disable add button;
            addButton.disabled = true;

            // Clear input fields;
            expensesTypeInput.value = '';
            amountInput.value = '';
            dateInput.value = '';
        }

        function buttonEditElementFunctionality() {
            // Get current li element;
            const currentLiElement = this.parentElement.parentElement;

            // Get article element & extract type, amount and date textContent;
            const articleElement = currentLiElement.querySelector('article');

            const pType = articleElement
                .querySelectorAll('p')[0].textContent
                .replace('Type: ', '');
            const pAmount = articleElement
                .querySelectorAll('p')[1].textContent
                .replace('Amount: ', '')
                .replace('$', '');
            const pDate = articleElement
                .querySelectorAll('p')[2].textContent
                .replace('Date: ', '');

            // Fill the input fields with the extracted type, amount and date;
            expensesTypeInput.value = pType;
            amountInput.value = Number(pAmount);
            dateInput.value = pDate;

            // Remove the li element from the ul element;
            currentLiElement.remove();

            // Enable add button;
            addButton.disabled = true;
        }

        function buttonOkElementFunctionality() {
            // Get current li element;
            const currentLiElement = this.parentElement.parentElement;

            // Get article element & extract type, amount and date textContent;
            const currentArticleElement = currentLiElement.querySelector('article');

            const pType = currentArticleElement.querySelectorAll('p')[0].textContent;
            const pAmount = currentArticleElement.querySelectorAll('p')[1].textContent;
            const pDate = currentArticleElement.querySelectorAll('p')[2].textContent;

            // Create p elements & set textContent;
            const pTypeElement = document.createElement('p');
            pTypeElement.textContent = `${pType}`

            const pAmountElement = document.createElement('p');
            pAmountElement.textContent = `${pAmount}`

            const pDateElement = document.createElement('p');
            pDateElement.textContent = `${pDate}`

            // Create article element & set append p elements;
            const articleElement = document.createElement('article');
            articleElement.appendChild(pTypeElement);
            articleElement.appendChild(pAmountElement);
            articleElement.appendChild(pDateElement);


            // Create li element & set class name & append article element;
            const liElement = document.createElement('li');
            liElement.className = 'expense-item';
            liElement.appendChild(articleElement);

            expensesList.appendChild(liElement);

            currentLiElement.remove();
        }
    }

    function deleteButtonFunctionality() {
        location.reload();
    }
}