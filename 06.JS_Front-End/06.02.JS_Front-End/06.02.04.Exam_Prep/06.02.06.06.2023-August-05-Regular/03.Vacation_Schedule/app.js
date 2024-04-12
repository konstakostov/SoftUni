const baseURL = 'http://localhost:3030/jsonstore/tasks'

let currentVacationID = null;

const nameInput = document.getElementById('name');
const daysInput = document.getElementById('num-days');
const dateInput = document.getElementById('from-date');

const listVacation = document.getElementById('list');

const loadVacations = document.getElementById('load-vacations');
loadVacations.addEventListener('click', loadVacationsFunctionality);

const addButton = document.getElementById('add-vacation');
addButton.addEventListener('click', async () => {
    // Create POST request;
    const response = await fetch(baseURL, {
        method: 'POST',
        headers: {
            'content-type': 'application/json',
        },
        body: JSON.stringify({
            name: nameInput.value,
            days: daysInput.value,
            date: dateInput.value,
        }),
    });

    // Check if POST request is valid;
    if (!response.ok) {
        return;
    }

    // Clear input fields;
    clearInputFields();

    await loadVacationsFunctionality();
})

const editButton = document.getElementById('edit-vacation');
editButton.addEventListener('click', async () => {
    // Make PUT request;
    const response = await fetch(`${baseURL}/${currentVacationID}`, {
        method: 'PUT',
        headers: {
            'content-type': 'application/json',
        },
        body: JSON.stringify({
            name: nameInput.value,
            days: daysInput.value,
            date: dateInput.value,
            _id: currentVacationID,
        })
    });

    // Check if PUT request is valid;
    if (!response.ok) {
        return;
    }

    // Deactivate editButton;
    editButton.disabled = true;

    // Activate addButton;
    addButton.disabled = false;

    // Clear the input fields;
    clearInputFields();

    // Clear currentVacationID;
    currentVacationID = null;

    // Load courses;
    await loadVacationsFunctionality();
})


async function loadVacationsFunctionality() {
    // Fetch all courses;
    const response = await fetch(baseURL);
    const data = await response.json();

    // Clear listVacation element;
    listVacation.innerHTML = '';

    // Create a course element for every object in data;
    for (const course of Object.values(data)) {
        // changeButton;
        const changeButton = document.createElement('button');
        changeButton.classList.add('change-btn');
        changeButton.textContent = 'Change';

        // doneButton;
        const doneButton = document.createElement('button');
        doneButton.classList.add('done-btn');
        doneButton.textContent = 'DYone';

        // h2Name;
        const h2Name = document.createElement('h2');
        h2Name.textContent = course.name;

        // h3Date;
        const h3Date = document.createElement('h3');
        h3Date.textContent = course.date;

        // h3Days;
        const h3Days = document.createElement('h3');
        h3Days.textContent = course.day;

        // courseContainer & Append elements to it;
        const courseContainer = document.createElement('div');
        courseContainer.classList.add('container');
        courseContainer.appendChild(h2Name);
        courseContainer.appendChild(h3Date);
        courseContainer.appendChild(h3Days);
        courseContainer.appendChild(changeButton);
        courseContainer.appendChild(doneButton);

        // Append courseContainer to listVacation;
        listVacation.appendChild(courseContainer);

        // Deactivate editButton;
        editButton.disabled = true;

        // changeButton addEventListener;
        changeButton.addEventListener('click', () => {
            // Get current course ID;
            currentVacationID = course._id;

            // Get course data & Populate input fields;
            nameInput.value = course.name;
            daysInput.value = course.days;
            dateInput.value = course.date;

            // Activate editButton;
            editButton.disabled = false;

            // Deactivate addButton;
            addButton.disabled = true;

            // Remove courseContainer from listVacation;
            courseContainer.remove();
        });

        // doneButton addEventListener;
        doneButton.addEventListener('click', async () => {
            // Create DELETE request;
            await fetch(`${baseURL}/${course._id}`, {
                method: 'DELETE',
            })

            // Check if DELETE request is valid;
            if (!response.ok) {
                return;
            }

            // Remove giftSock from mealList;
            courseContainer.remove();
        })
    }
}

function clearInputFields() {
    nameInput.value = '';
    daysInput.value = '';
    dateInput.value = '';
}