const baseURL = 'http://localhost:3030/jsonstore/tasks'

let currentWeatherID = null;

const locationInput = document.getElementById('location');
const temperatureInput = document.getElementById('temperature');
const dateInput = document.getElementById('date');

const listWeather = document.getElementById('list');

const loadHistory = document.getElementById('load-history');
loadHistory.addEventListener('click', loadHistoryFunctionality);

const addButton = document.getElementById('add-weather');
addButton.addEventListener('click', async () => {
    // Create POST request;
    const response = await fetch(baseURL, {
        method: 'POST',
        headers: {
            'content-type': 'application/json',
        },
        body: JSON.stringify({
            location: locationInput.value,
            temperature: temperatureInput.value,
            date: dateInput.value,
        }),
    });

    // Check if POST request is valid;
    if (!response.ok) {
        return;
    }

    // Clear input fields;
    clearInputFields();

    await loadHistoryFunctionality();
})

const editButton = document.getElementById('edit-weather');
editButton.addEventListener('click', async () => {
    // Make PUT request;
    const response = await fetch(`${baseURL}/${currentWeatherID}`, {
        method: 'PUT',
        headers: {
            'content-type': 'application/json',
        },
        body: JSON.stringify({
            location: locationInput.value,
            temperature: temperatureInput.value,
            date: dateInput.value,
            _id: currentWeatherID,
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

    // Clear currentMealID;
    currentPresentID = null;

    // Load Meals;
    await loadHistoryFunctionality();
})

async function loadHistoryFunctionality() {
    // Fetch all records;
    const response = await fetch(baseURL);
    const data = await response.json();

    // Clear giftList element;
    listWeather.innerHTML = '';

    // Create a weather element for every object in data;
    for (const weather of Object.values(data)) {
        // changeButton;
        const changeButton = document.createElement('button');
        changeButton.classList.add('change-btn');
        changeButton.textContent = 'Change';

        // deleteButton;
        const deleteButton = document.createElement('button');
        deleteButton.classList.add('delete-btn');
        deleteButton.textContent = 'Delete';

        // buttonsContainer & Append buttons;
        const buttonsContainer = document.createElement('div');
        buttonsContainer.classList.add('buttons-container');
        buttonsContainer.appendChild(changeButton);
        buttonsContainer.appendChild(deleteButton);

        // pGift;
        const h2Location = document.createElement('p');
        h2Location.textContent = weather.location;

        // pFor;
        const h3Date = document.createElement('p');
        h3Date.textContent = weather.date;

        // pPrice;
        const h3Temperature = document.createElement('p');
        h3Temperature.textContent = weather.temperature;
        h3Temperature.id = 'celsius';

        const weatherContainer = document.createElement('div');
        weatherContainer.classList.add('container');
        weatherContainer.appendChild(h2Location);
        weatherContainer.appendChild(h3Date);
        weatherContainer.appendChild(h3Temperature);
        weatherContainer.appendChild(buttonsContainer);

        // Append weatherContainer to listWeather;
        listWeather.appendChild(weatherContainer);

        // Deactivate editButton;
        editButton.disabled = true;

        // changeButton addEventListener;
        changeButton.addEventListener('click', () => {
            // Get current weather ID;
            currentWeatherID = weather._id;

            // Get presents data & Populate input fields;
            locationInput.value = weather.location;
            temperatureInput.value = weather.temperature;
            dateInput.value = weather.date;

            // Activate editButton;
            editButton.disabled = false;

            // Deactivate addButton;
            addButton.disabled = true;

            // Remove giftSock from mealList;
            weatherContainer.remove();
        })

        // deleteButton addEventListener;
        deleteButton.addEventListener('click', async () => {
            // Create DELETE request;
            await fetch(`${baseURL}/${weather._id}`, {
                method: 'DELETE',
            })

            // Check if DELETE request is valid;
            if (!response.ok) {
                return;
            }

            // Remove giftSock from mealList;
            weatherContainer.remove();
        })
    }
}

function clearInputFields() {
    locationInput.value = '';
    temperatureInput.value = '';
    dateInput.value = '';
}