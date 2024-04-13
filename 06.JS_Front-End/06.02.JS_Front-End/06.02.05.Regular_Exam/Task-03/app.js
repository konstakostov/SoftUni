const baseURL = 'http://localhost:3030/jsonstore/games';

let currentGameID = null;

const nameInput = document.getElementById('g-name');
const typeInput = document.getElementById('type');
const playersInput = document.getElementById('players');

const gamesList = document.getElementById('games-list');

const loadGames = document.getElementById('load-games');
loadGames.addEventListener('click', loadGamesFunctionality);

const addGameButton = document.getElementById('add-game');
addGameButton.addEventListener('click', async () => {
    // Create POST request;
    const response = await fetch(baseURL, {
        method: 'POST',
        headers: {
            'content-type': 'application/json',
        },
        body: JSON.stringify({
            name: nameInput.value,
            type: typeInput.value,
            players: playersInput.value,
        }),
    });

    // Check if POST request is valid;
    if (!response.ok) {
        return;
    }

    // Clear input fields;
    clearInputFields();

    await loadGamesFunctionality();
})

const editGameButton = document.getElementById('edit-game');
editGameButton.addEventListener('click', async () => {
    // Make PUT request;
    const response = await fetch(`${baseURL}/${currentGameID}`, {
        method: 'PUT',
        headers: {
            'content-type': 'application/json',
        },
        body: JSON.stringify({
            name: nameInput.value,
            type: typeInput.value,
            players: playersInput.value,
            _id: currentGameID,
        })
    });

    // Check if PUT request is valid;
    if (!response.ok) {
        return;
    }

    // Deactivate editGameButton;
    editGameButton.disabled = true;

    // Activate addGameButton;
    addGameButton.disabled = false;

    // Clear the input fields;
    clearInputFields();

    // Clear currentGameID;
    currentGameID = null;

    // Load ;
    await loadGamesFunctionality();
})

async function loadGamesFunctionality() {
    // Fetch all records;
    const response = await fetch(baseURL);
    const data = await response.json();

    // Clear gamesList element;
    gamesList.innerHTML = '';

    // Create a game element for every object in data;
    for (const game of Object.values(data)) {
        // changeButton;
        const changeButton = document.createElement('button');
        changeButton.classList.add('change-btn');
        changeButton.textContent = 'Change';

        // deleteButton;
        const deleteButton= document.createElement('button');
        deleteButton.classList.add('delete-btn');
        deleteButton.textContent = 'Delete';

        // buttonsContainer & Append buttons;
        const buttonsContainer = document.createElement('div');
        buttonsContainer.classList.add('buttons-container');
        buttonsContainer.appendChild(changeButton);
        buttonsContainer.appendChild(deleteButton);

        // pName;
        const pName = document.createElement('p');
        pName.textContent = game.name;

        // pPlayers;
        const pPlayers = document.createElement('p');
        pPlayers.textContent = game.players;

        // pType;
        const pType = document.createElement('p');
        pType.textContent = game.type;

        // gamesContent & Append pName, pPlayers, pType;
        const gamesContent = document.createElement('div');
        gamesContent.classList.add('content');
        gamesContent.appendChild(pName);
        gamesContent.appendChild(pPlayers);
        gamesContent.appendChild(pType);

        // boardGame & Append gamesContent and buttonsContainer;
        const boardGame= document.createElement('div');
        boardGame.classList.add('board-game');
        boardGame.appendChild(gamesContent);
        boardGame.appendChild(buttonsContainer);

        // Append boardGame to gamesList;
        gamesList.appendChild(boardGame);

        // Deactivate editGameButton;
        editGameButton.disabled = true;

        // changeButton addEventListener;
        changeButton.addEventListener('click', () => {
            // Get current game ID;
            currentGameID = game._id;

            // Get game data & Populate input fields;
            nameInput.value = game.name;
            typeInput.value = game.type;
            playersInput.value = game.players;

            // Activate editGameButton;
            editGameButton.disabled = false;

            // Deactivate addGameButton;
            addGameButton.disabled = true;

            // Remove boardGame from gamesList;
            boardGame.remove();
        })

        // deleteButton addEventListener;
        deleteButton.addEventListener('click', async () => {
            // Create DELETE request;
            await fetch(`${baseURL}/${game._id}`, {
                method: 'DELETE',
            })

            // Check if DELETE request is valid;
            if (!response.ok) {
                return;
            }

            // Remove boardGame from gamesList;
            boardGame.remove();
        })
    }
}

// Clear all input field values;
function clearInputFields() {
    nameInput.value = '';
    typeInput.value = '';
    playersInput.value = '';
}