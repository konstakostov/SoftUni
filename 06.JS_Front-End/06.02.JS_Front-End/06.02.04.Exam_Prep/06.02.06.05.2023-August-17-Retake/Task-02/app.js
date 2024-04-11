window.addEventListener("load", solve);

function solve() {
    const playerInput = document.getElementById('player');
    const scoreInput = document.getElementById('score');
    const roundInput = document.getElementById('round');

    const sureList = document.getElementById('sure-list');

    const scoreboardList = document.getElementById('scoreboard-list')

    const addButton = document.getElementById('add-btn');
    addButton.addEventListener('click', addButtonFunctionality);

    const playerContainer = document.getElementById('players-container');
    const clearButton = playerContainer.querySelector('button');
    clearButton.addEventListener('click', () => {
        window.location.reload();
    })

    function addButtonFunctionality() {
        const player = playerInput.value;
        const score = scoreInput.value;
        const round = roundInput.value;

        if (player !== '' && score !== '' && round !== '') {
            // editButton;
            const editButton = document.createElement('button');
            editButton.className = 'btn edit';
            editButton.textContent = 'edit';

            // okButton;
            const okButton = document.createElement('button');
            okButton.className = 'btn ok';
            okButton.textContent = 'ok';

            // pName;
            const pName = document.createElement('p');
            pName.textContent = player;

            // pScore;
            const pScore = document.createElement('p');
            pScore.textContent = `Score: ${score}`;

            // pRound;
            const pRound = document.createElement('p');
            pRound.textContent = `Round: ${round}`;

            // articleContainer & append pName, pScore, pRound;
            const articleContainer = document.createElement('article');
            articleContainer.appendChild(pName);
            articleContainer.appendChild(pScore);
            articleContainer.appendChild(pRound);

            // dartItem & append buttonContainer, articleContainer;
            const dartItem = document.createElement('li');
            dartItem.classList.add('dart-item');
            dartItem.appendChild(articleContainer);
            dartItem.appendChild(editButton);
            dartItem.appendChild(okButton);


            // Append dartItem to sureList;
            sureList.appendChild(dartItem);

            // Disable addButton;
            addButton.disabled = true;

            // Clear input fields;
            clearInputFields();

            // editButton addEventListener;
            editButton.addEventListener('click', () => {
                // Fill input fields;
                playerInput.value = player;
                scoreInput.value = score;
                roundInput.value = round;

                // Enable addButton;
                addButton.disabled = false;

                // Remove dartItem;
                dartItem.remove();
            })

            // okButton addEventListener;
            okButton.addEventListener('click', () => {
                // Remove editButton and okButton
                editButton.remove()
                okButton.remove()

                console.log(dartItem);


                // Append dartItem to scoreboardList;
                scoreboardList.appendChild(dartItem);

                // Clear sureList children elements;
                sureList.innerHTML = ''

                // Enable addButton;
                addButton.disabled = false;

                console.log(scoreboardList);
            })
        }
    }

    function clearInputFields() {
        playerInput.value = '';
        scoreInput.value = '';
        roundInput.value = '';
    }
}
