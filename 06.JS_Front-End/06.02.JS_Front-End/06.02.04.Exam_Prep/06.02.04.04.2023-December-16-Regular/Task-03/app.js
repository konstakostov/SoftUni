const baseURL = 'http://localhost:3030/jsonstore/tasks/';

let currentMealID = '';

const loadMeals = document.getElementById('load-meals');
loadMeals.addEventListener('click', loadMealsFunctionality);

const editMeal = document.getElementById('edit-meal');
editMeal.addEventListener('click', editMealFunctionality);

const addMeal = document.getElementById('add-meal');
addMeal.addEventListener('click', addMealFunctionality);

const divList = document.getElementById('list');

const foodInput = document.getElementById('food');
const timeInput = document.getElementById('time');
const caloriesInput = document.getElementById('calories');

async function loadMealsFunctionality() {
    const tasksRequest = await fetch(baseURL);
    const tasks = await tasksRequest.json();

    divList.innerHTML = '';

    for (const taskID in tasks) {
        // Create h2Food element & set textContent;
        const h2Food = document.createElement('h2');
        h2Food.textContent = tasks[taskID].food;

        // Create h3Time element & set textContent;
        const h3Time = document.createElement('h3');
        h3Time.textContent = tasks[taskID].time;

        // Create h3Calories element & set textContent;
        const h3Calories = document.createElement('h3');
        h3Calories.textContent = tasks[taskID].calories;

        // Create button change-meal element & set textContent & addCLickEvent;
        const changeMealButton = document.createElement('button');
        changeMealButton.className = 'change-meal';
        changeMealButton.textContent = 'Change';
        changeMealButton.addEventListener('click', changeMealButtonFunctionality);

        // Create button delete-meal element & set textContent & addCLickEvent;
        const deleteMealButton = document.createElement('button');
        deleteMealButton.className = 'delete-meal';
        deleteMealButton.textContent = 'Delete';
        deleteMealButton.addEventListener('click', deleteMealButtonFunctionality);

        // Create div meal-buttons element & append button elements (changeMealButton & deleteMealButton);
        const divMealButtons = document.createElement('div');
        divMealButtons.id = 'meal-buttons';
        divMealButtons.appendChild(changeMealButton);
        divMealButtons.appendChild(deleteMealButton);

        // Create a div meal element & append h2Food, h3Food, h3Calories, divMealButtons elements;
        const divMeal = document.createElement('div');
        divMeal.className = 'meal';
        divMeal.id = tasks[taskID]._id;

        divMeal.appendChild(h2Food);
        divMeal.appendChild(h3Time);
        divMeal.appendChild(h3Calories);
        divMeal.appendChild(divMealButtons);

        // Deactivating EditMeal button;
        editMeal.disabled = true;

        // Adding every divMeal element to divList element;
        divList.appendChild(divMeal);
    }

    function changeMealButtonFunctionality() {
        // Get the current meal div element & it's id;
        const currentDivMeal = this.parentElement.parentElement;
        currentMealID = currentDivMeal._id;

        // Disable the editMeal button & enable the editMeal button;
        editMeal.disabled = false;
        addMeal.disabled = true;

        // Take the values from the current Meal Plan for the meal, time and calories input fields;
        const currentMeal = currentDivMeal.querySelector('h2').textContent;
        const currentTime = currentDivMeal.querySelectorAll('h3')[0].textContent;
        const currentCalories = currentDivMeal.querySelectorAll('h3')[1].textContent;

        // Set the input fields with the appropriate values;
        foodInput.value = currentMeal;
        timeInput.value = currentTime;
        caloriesInput.value = currentCalories;

        // Remove the current div element from the DOM tree;
        currentDivMeal.remove();
    }

    async function deleteMealButtonFunctionality() {
        // Get the current meal div element & its id;
        const currentDivMeal = this.parentElement.parentElement;
        const currentMealID = currentDivMeal.id;

        currentDivMeal.remove();
        divList.innerHTML = '';

        const deleteURL = baseURL + currentMealID;

        try {
            // Make a DELETE request to the server
            const deleteResponse = await fetch(deleteURL, {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json'
                },
            });

            // Check if the delete request was successful
            if (deleteResponse.ok) {
                // If successful, reload the meals
                await loadMealsFunctionality();
            } else {
                // If unsuccessful, handle the error
                console.error('Failed to delete meal:', deleteResponse.statusText);
            }
        } catch (error) {
            // Handle any network errors
            console.error('Error deleting meal:', error);
        }
    }

}

async function editMealFunctionality() {
    // Get the current meal task id;
    const _idMeal = currentMealID;

    // Create an updated meal object;
    const updatedMeal = {
        food: foodInput.value,
        calories: caloriesInput.value,
        time: timeInput.value,
    }

    // Make a PUT request at the local server;
    const mealUpdateResponse = await fetch(baseURL + _idMeal, {
        method: "PUT",
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(updatedMeal),
    });

    // if the meal update is successful, load the meals again;
    if (mealUpdateResponse.ok) {
        await loadMealsFunctionality;
    }

    // Clear the input values
    foodInput.value = '';
    caloriesInput.value = '';
    timeInput.value = '';

    // Enable the editMeal button & disable the editMeal button;
    editMeal.disabled = true;
    addMeal.disabled = false;
}

async function addMealFunctionality() {
    // Get foodInput, timeInput, caloriesInput values & create id value
    const food = foodInput.value;
    const time = timeInput.value;
    const calories = caloriesInput.value;

    // Create newTask object;
    const newTask = {
        food: food,
        calories: calories,
        time: time,
    }

    // Check if food, time and calories are not empty & make POST request with newTask Object;
    if (food !== '' && time !== '' && calories !== '') {
        // Create POST request;
        const mealPOST = await fetch(baseURL, {
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(newTask),
        })

        // Check if the POST request is successful;
        if (mealPOST.ok) {
            // Get all Meals Tasks from server;
            await loadMealsFunctionality

            // Clear input fields;
            foodInput.value = '';
            timeInput.value = '';
            caloriesInput.value = '';
        }
    }
}