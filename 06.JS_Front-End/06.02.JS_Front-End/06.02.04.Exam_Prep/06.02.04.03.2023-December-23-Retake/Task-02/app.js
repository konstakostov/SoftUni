window.addEventListener("load", solve);

function solve() {
    const placeInput = document.getElementById('place');
    const actionInput = document.getElementById('action');
    const personInput = document.getElementById('person');

    const taskList = document.getElementById('task-list');
    const taskDone = document.getElementById('done-list');

    const addButton = document.getElementById('add-btn');
    addButton.addEventListener('click', addButtonFunctionality);

    function addButtonFunctionality() {
        if (placeInput.value !== '' && actionInput.value !== '' && personInput.value !== '') {
            // Create paragraphs elements;
            const pPlaceElement = document.createElement('p');
            pPlaceElement.textContent = `Place:${placeInput.value}`;

            const pActionElement = document.createElement('p');
            pActionElement.textContent = `Action:${actionInput.value}`;

            const pPersonElement = document.createElement('p');
            pPersonElement.textContent = `Person:${personInput.value}`;

            // Create article element & append paragraph elements;
            const articleElement = document.createElement('article');
            articleElement.appendChild(pPlaceElement);
            articleElement.appendChild(pActionElement);
            articleElement.appendChild(pPersonElement);

            // Create button elements;
            const buttonEdit = document.createElement('button');
            buttonEdit.className = 'edit';
            buttonEdit.textContent = 'Edit';
            buttonEdit.addEventListener('click', buttonEditFunctionality);

            const buttonDone = document.createElement('button');
            buttonDone.className = 'done';
            buttonDone.textContent = 'Done';
            buttonDone.addEventListener('click', () => {
                buttonDoneFunctionality(buttonDone);
            });

            // Create div element & append buttons elements;
            const divButtonsElement = document.createElement('div');
            divButtonsElement.className = 'buttons';
            divButtonsElement.appendChild(buttonEdit);
            divButtonsElement.appendChild(buttonDone);

            // Create list element & append article, div elements;
            const liElement = document.createElement('li')
            liElement.className = 'clean-task';
            liElement.appendChild(articleElement);
            liElement.appendChild(divButtonsElement);

            // Append li element to ul element;
            taskList.appendChild(liElement);

            // Clear input fields;
            placeInput.value = '';
            actionInput.value = '';
            personInput.value = '';
        }
    }

    function buttonEditFunctionality() {
        const cleaningTasks = document.querySelector('article');

        const place = cleaningTasks
            .querySelectorAll('p')[0].textContent
            .replace('Place:', '');
        const action = cleaningTasks
            .querySelectorAll('p')[1].textContent
            .replace('Action:', '');
        const person = cleaningTasks
            .querySelectorAll('p')[2].textContent
            .replace('Person:', '');

        placeInput.value = place;
        actionInput.value = action;
        personInput.value = person;

        cleaningTasks.parentElement.remove();
    }

    function buttonDoneFunctionality(button) {
        const cleaningTasks = button.parentElement.parentElement;

        const buttonsElement = cleaningTasks.querySelectorAll('button');
        buttonsElement.forEach(button => {
            if (button !== this) {
                button.remove();
            }
        });

        // Create the delete button
        const buttonDelete = document.createElement('button');
        buttonDelete.className = 'delete';
        buttonDelete.textContent = 'Delete';

        // Create a div element for buttons and append the delete button
        const divButtonsElement = document.createElement('div');
        divButtonsElement.className = 'buttons';
        divButtonsElement.appendChild(buttonDelete);

        // Replace the existing buttons div with the new one
        const existingButtonsDiv = cleaningTasks.querySelector('.buttons');
        existingButtonsDiv.replaceWith(divButtonsElement);

        // Move the task to the done list
        taskDone.appendChild(cleaningTasks);
        cleaningTasks.remove();
    }
}