window.addEventListener("load", solve);

function solve() {
    // Input field elements;
    const placeInput = document.getElementById('place');
    const actionInput = document.getElementById('action');
    const personInput = document.getElementById('person');

    // Task list element;
    const taskList = document.getElementById('task-list');

    // Done list element;
    const doneList = document.getElementById('done-list');

    // Add button element & addEventListener;
    const addButton = document.getElementById('add-btn');
    addButton.addEventListener('click', () => {
        const place = placeInput.value;
        const action = actionInput.value;
        const person = personInput.value;

        if (place !== '' && action !== '' && person !== '') {
            // Create editButton;
            const editButton = document.createElement('button');
            editButton.classList.add('edit');
            editButton.textContent = 'Edit';

            // Create doneButton;
            const doneButton = document.createElement('button');
            doneButton.classList.add('done');
            doneButton.textContent = 'Done';

            // Create buttonContainer & Append buttons (editButton, doneButton);
            const buttonContainer = document.createElement('div');
            buttonContainer.classList.add('buttons');
            buttonContainer.appendChild(editButton);
            buttonContainer.appendChild(doneButton);

            // Create pPlace;
            const pPlace = document.createElement('p');
            pPlace.textContent = `Place:${place}`;

            // Create pAction;
            const pAction = document.createElement('p');
            pAction.textContent = `Action:${action}`;

            // Create pPerson;
            const pPerson = document.createElement('p');
            pPerson.textContent = `Person:${person}`;

            // Create articleContainer;
            const articleContainer = document.createElement('article');
            articleContainer.appendChild(pPlace);
            articleContainer.appendChild(pAction);
            articleContainer.appendChild(pPerson);

            // Create cleanTask;
            const cleanTask = document.createElement('li');
            cleanTask.classList.add('clean-task');
            cleanTask.appendChild(articleContainer);
            cleanTask.appendChild(buttonContainer);

            // Add cleanTask to taskList;
            taskList.appendChild(cleanTask);

            // Clean input fields;
            clearInputFields();

            // editButton addEventListener
            editButton.addEventListener('click', () => {
                // Fill input fields with current task data;
                placeInput.value = place;
                actionInput.value = action;
                personInput.value = person;

                // Remove cleanTask from taskList;
                cleanTask.remove();
            })

            // doneButton addEventListener
            doneButton.addEventListener('click', () => {
                // Get buttonContainer & Remove it from cleanTask
                const divElement = cleanTask.querySelector('div')
                divElement.remove();

                // Create deleteButton;
                const deleteButton = document.createElement('button');
                deleteButton.classList.add('delete');
                deleteButton.textContent = 'Delete';

                // Remove classList from cleanTask;
                cleanTask.classList.remove('clean-task');

                // Add deleteButton to cleanTask
                cleanTask.appendChild(deleteButton);

                // Remove cleanTask from taskList;
                cleanTask.remove();

                // Add cleanTask to doneList;
                doneList.appendChild(cleanTask);

                // deleteButton addEventListener;
                deleteButton.addEventListener('click', () => {
                    cleanTask.remove();
                })
            })
        }
    })

    // Clear input fields;
    function clearInputFields() {
        placeInput.value = '';
        actionInput.value = '';
        personInput.value = '';
    }
}