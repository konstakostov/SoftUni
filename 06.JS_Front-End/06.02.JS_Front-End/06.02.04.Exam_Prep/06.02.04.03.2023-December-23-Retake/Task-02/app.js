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
            buttonDone.addEventListener('click', buttonDoneFunctionality);

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
        const currentTask = this.parentElement.parentElement;

        const place = currentTask
            .querySelector('p:nth-of-type(1)').textContent
            .split(':')[1]
            .trim();
        const action = currentTask
            .querySelector('p:nth-of-type(2)').textContent
            .split(':')[1]
            .trim();
        const person = currentTask
            .querySelector('p:nth-of-type(3)').textContent
            .split(':')[1]
            .trim();


        placeInput.value = place;
        actionInput.value = action;
        personInput.value = person;

        currentTask.remove();
    }

    function buttonDoneFunctionality() {
        const currentButton = this
        const currentTask = currentButton.parentElement.parentElement;
        const buttonsToRemove = currentTask.querySelectorAll("button")
        buttonsToRemove.forEach(button => {
            button.remove();
        });

        const deleteButton = document.createElement('button');
        deleteButton.textContent = 'Delete';
        deleteButton.addEventListener('click', deleteButtonFunctionality)

        const divElement = currentTask.querySelector("div");
        divElement.appendChild(deleteButton);

        currentTask.remove();

        taskDone.appendChild(currentTask);
    }

    function deleteButtonFunctionality() {
        const taskToDelete = this.parentElement.parentElement;
        taskToDelete.remove();
    }
}