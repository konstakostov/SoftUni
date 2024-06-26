const baseURL = 'http://localhost:3030/jsonstore/gifts';

let currentPresentID = null;

const giftInput = document.getElementById('gift');
const forInput = document.getElementById('for');
const priceInput = document.getElementById('price');

const giftList = document.getElementById('gift-list');

const addButton = document.getElementById('add-present');
addButton.addEventListener('click', async () => {
    // Create POST request;
    const response = await fetch(baseURL, {
        method: 'POST',
        headers: {
            'content-type': 'application/json',
        },
        body: JSON.stringify({
            gift: giftInput.value,
            for: forInput.value,
            price: priceInput.value,
        }),
    });

    // Check if POST request is valid;
    if (!response.ok) {
        return;
    }

    // Clear input fields;
    clearInputFields();

    await loadPresentsFunctionality();
})

const editButton = document.getElementById('edit-present');
editButton.addEventListener('click', async () => {
    // Make PUT request;
    const response = await fetch(`${baseURL}/${currentPresentID}`, {
        method: 'PUT',
        headers: {
            'content-type': 'application/json',
        },
        body: JSON.stringify({
            gift: giftInput.value,
            for: forInput.value,
            price: priceInput.value,
            _id: currentPresentID,
        })
    });

    // Check if PUT request is valid;
    if (!response.ok) {
        return;
    }

    // Load Meals;
    await loadPresentsFunctionality();

    // Deactivate editButton;
    editButton.disabled = true;

    // Activate addButton;
    addButton.disabled = false;

    // Clear the input fields;
    clearInputFields();

    // Clear currentMealID;
    currentPresentID = null;
})

const loadPresents = document.getElementById('load-presents');
loadPresents.addEventListener('click', loadPresentsFunctionality);

async function loadPresentsFunctionality() {
    // Fetch all presents;
    const response = await fetch(baseURL);
    const data = await response.json();

    // Clear giftList element;
    giftList.innerHTML = '';

    // Create a gift element for every object in data;
    for (const present of Object.values(data)) {
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
        const pGift = document.createElement('p');
        pGift.textContent = present.gift;

        // pFor;
        const pFor = document.createElement('p');
        pFor.textContent = present.for;

        // pPrice;
        const pPrice = document.createElement('p');
        pPrice.textContent = present.price;

        // contentContainer & Append p elements;
        const contentContainer = document.createElement('div');
        contentContainer.classList.add('content');
        contentContainer.appendChild(pGift);
        contentContainer.appendChild(pFor);
        contentContainer.appendChild(pPrice);

        // giftSock & Append contentContainer and buttonsContainer;
        const giftSock = document.createElement('div');
        giftSock.classList.add('gift-sock');
        giftSock.appendChild(contentContainer);
        giftSock.appendChild(buttonsContainer);

        // Append giftSock to giftList;
        giftList.appendChild(giftSock)

        // Deactivate editButton;
        editButton.disabled = true;

        // changeButton addEventListener;
        changeButton.addEventListener('click', () => {
            currentPresentID = present._id;

            // Get presents data & Populate input fields;
            giftInput.value = present.gift;
            forInput.value = present.for;
            priceInput.value = present.price;

            // Activate editButton;
            editButton.disabled = false;

            // Deactivate addButton;
            addButton.disabled = true;

            // Remove giftSock from mealList;
            giftSock.remove();
        })

        // deleteButton addEventListener;
        deleteButton.addEventListener('click', async () => {
            // Create DELETE request;
            await fetch(`${baseURL}/${present._id}`, {
                method: 'DELETE',
            })

            // Check if DELETE request is valid;
            if (!response.ok) {
                return;
            }

            // Remove giftSock from mealList;
            giftSock.remove();
        })
    }
}

function clearInputFields() {
    giftInput.value = '';
    forInput.value = '';
    priceInput.value = '';
}