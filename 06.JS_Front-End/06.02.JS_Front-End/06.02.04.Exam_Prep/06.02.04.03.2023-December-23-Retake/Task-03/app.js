const baseURL = 'http://localhost:3030/jsonstore/gifts/';
let presentToEditID = '';

const giftList = document.getElementById('gift-list');

const newGift = document.getElementById('gift');
const newFor = document.getElementById('for');
const newPrice = document.getElementById('price');

const loadButton = document.getElementById('load-presents');
loadButton.addEventListener('click', loadButtonFunctionality);

const editButton = document.getElementById('edit-present');
editButton.addEventListener('click', () => {
    editButtonFunctionality(presentToEditID)
});

const addButton = document.getElementById('add-present');
addButton.addEventListener('click', addButtonFunctionality);


async function editButtonFunctionality(presentID) {
    const _idPresent = presentID;

    const updatedPresent = {
        gift: newGift.value,
        for: newFor.value,
        price: newPrice.value,
    }

    const presentUpdateResponse = await fetch(baseURL + _idPresent, {
        method: "PUT",
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(updatedPresent),
    });

    if (presentUpdateResponse.ok) {
        await loadButtonFunctionality();
    }

    newGift.value = '';
    newFor.value = '';
    newPrice.value = '';
    editButton.disabled = true;
    addButton.disabled = false;
}

async function loadButtonFunctionality() {
    const presentRecordsFetch = await fetch(baseURL);
    const presentRecords = await presentRecordsFetch.json();

    giftList.innerHTML = '';

    for (const presentId in presentRecords) {
        const divElement = document.createElement('div');
        divElement.className = 'gift-sock';

        divElement.innerHTML = `
            <div class="content" id="${presentRecords[presentId]._id}">
                <p>"${presentRecords[presentId].gift}"</p>
                <p>"${presentRecords[presentId].for}"</p>
                <p>"${presentRecords[presentId].price}"</p>
            </div>
            <div class="buttons-container">
                <button class="change-btn">Change</button>
                <button class="delete-btn">Delete</button>
            </div>
        `
        giftList.appendChild(divElement);

        const changeButtons = document.querySelectorAll('.change-btn');
        changeButtons.forEach(button => {
            button.addEventListener('click', changeButtonFunctionality);
        });

        const deleteButtons = document.querySelectorAll('.delete-btn');
        deleteButtons.forEach(button => {
            button.addEventListener('click', deleteButtonFunctionality);
        });
    }

    async function deleteButtonFunctionality() {
        const currentPresent = this.parentElement.parentElement;
        const presentContent = currentPresent.querySelector('div');

        presentToEditID = presentContent.id.toString();

        const deleteResponse = await fetch(baseURL + presentToEditID, {
            method: 'DELETE'
        });

        if (deleteResponse.ok) {
            await loadButtonFunctionality();
        }
    }

    function changeButtonFunctionality() {
        const currentPresent = this.parentElement.parentElement;
        const presentContent = currentPresent.querySelector('div');

        presentToEditID = presentContent.id.toString();

        const giftContent = presentContent.querySelectorAll('p')[0].textContent.replace(/"/g, '');
        const forContent = presentContent.querySelectorAll('p')[1].textContent.replace(/"/g, '');
        const priceContent = presentContent.querySelectorAll('p')[2].textContent.replace(/"/g, '');

        newGift.value = giftContent;
        newFor.value = forContent;
        newPrice.value = priceContent;

        currentPresent.remove()

        editButton.disabled = false;
        addButton.disabled = true;
    }
}

async function addButtonFunctionality() {
    const newPresent = {
        gift: newGift.value.trim(),
        for: newFor.value.trim(),
        price: newPrice.value.trim(),
    }

    const addGiftResponse = await fetch(baseURL, {
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(newPresent),
    })

    if (addGiftResponse.ok) {
        await loadButtonFunctionality();

        newGift.value = '';
        newFor.value = '';
        newPrice.value = '';
    }
}