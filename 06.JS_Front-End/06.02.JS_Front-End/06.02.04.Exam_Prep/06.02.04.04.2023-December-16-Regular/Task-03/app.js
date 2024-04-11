// Base url for fetch requests;
const baseURL = 'http://localhost:3030/jsonstore/tasks';

// Current Meal ID; Set when changeButton is pressed;
let currentMealID = null;

// Input fields for food, time and calories;
const foodInput = document.getElementById('food');
const timeInput = document.getElementById('time');
const caloriesInput = document.getElementById('calories');

// Meal List Element;
const mealList = document.getElementById('list');

// Load Button & addEventListener;
const loadButton = document.getElementById('load-meals');
loadButton.addEventListener('click', loadButtonFunctionality);

// Edit Meal Button Element;
const editButton = document.getElementById('edit-meal');
editButton.addEventListener('click', async () => {
    // Get the fields input data;
    const {food, calories, time} = getInputFields();

    // Make PUT request;
    const response = await fetch(`${baseURL}/${currentMealID}`, {
        method: 'PUT',
        headers: {
            'content-type': 'application/json',
        },
        body: JSON.stringify({
            _id: currentMealID,
            food,
            calories,
            time,
        })
    });

    if (!response.ok) {
        return;
    }

    // Load Meals;
    await loadButtonFunctionality();

    // Deactivate editButton;
    editButton.disabled = true;

    // Activate addButton;
    addButton.disabled = false;

    // Clear the input fields;
    clearInputFields();

    // Clear currentMealID;
    currentMealID = null;
})

// Add Meal Button Element;
const addButton = document.getElementById('add-meal');
addButton.addEventListener('click', async () => {
    // Get the fields input data;
    const newMeal = getInputFields();

    // Create POST request;
    const response = await fetch(baseURL, {
        method: 'POST',
        headers: {
            'content-type': 'application/json',
        },
        body: JSON.stringify(newMeal),
    });

    if (!response.ok) {
        return;
    }

    // Clear the input fields;
    clearInputFields();

    // Load all meals;
    /* NB!
        BECAUSE OF await THE TEST DID NOT PASS THE SECOND TEST & WAS LOOKING IF ALL THE FIELDS WERE CLEARED AND THEY
        WERE NOT...
     */
    await loadButtonFunctionality();
})

async function loadButtonFunctionality() {
    // Fetch all meals;
    const response = await fetch(baseURL);
    const data = await response.json();

    // Clear mealList element;
    mealList.innerHTML = '';

    // Create a meal element for object of data;
    for (const meal of Object.values(data)) {
        const changeButton = document.createElement('button');
        changeButton.classList.add('change-meal');
        changeButton.textContent = 'Change';

        const deleteButton = document.createElement('button');
        deleteButton.classList.add('delete-meal');
        deleteButton.textContent = 'Delete';

        const buttonContainer = document.createElement('div');
        buttonContainer.id = 'meal-buttons';
        buttonContainer.appendChild(changeButton);
        buttonContainer.appendChild(deleteButton);

        const foodH2Element = document.createElement('h2');
        foodH2Element.textContent = meal.food;

        const timeH3Element = document.createElement('h3');
        timeH3Element.textContent = meal.time;

        const calorieH3Element = document.createElement('h3');
        calorieH3Element.textContent = meal.calories;

        const mealElement = document.createElement('div');
        mealElement.classList.add('meal')
        mealElement.appendChild(foodH2Element);
        mealElement.appendChild(timeH3Element);
        mealElement.appendChild(calorieH3Element);
        mealElement.appendChild(buttonContainer);

        // Append meal to mealList;
        mealList.appendChild(mealElement);

        // changeButton addEventListener;
        changeButton.addEventListener('click', () => {
            // Save current meal ID;
            currentMealID = meal._id;

            // Get meal data & Populate input fields;
            foodInput.value = meal.food;
            timeInput.value = meal.time;
            caloriesInput.value = meal.calories;

            // Activate editButton;
            editButton.disabled = false;

            // Deactivate addButton;
            addButton.disabled = true;

            // Remove mealElement from mealList;
            mealElement.remove();
        })

        // deleteButton addEventListener;
        deleteButton.addEventListener('click', async () => {
            // Create DELETE request;
            await fetch(`${baseURL}/${meal._id}`, {
                method: 'DELETE',
            })

            if (!response.ok) {
                return;
            }

            // Remove mealElement from mealList;
            mealElement.remove();
        })
    }
}

// Get all input values;
function getInputFields() {
    const food = foodInput.value;
    const time = timeInput.value;
    const calories = caloriesInput.value;

    return {food, time, calories}
}


// Clear all input values;
function clearInputFields() {
    foodInput.value = '';
    timeInput.value = '';
    caloriesInput.value = '';
}