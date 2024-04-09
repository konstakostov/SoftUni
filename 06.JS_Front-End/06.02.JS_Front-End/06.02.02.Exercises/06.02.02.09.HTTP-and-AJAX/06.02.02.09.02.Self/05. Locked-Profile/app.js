async function lockedProfile() {
    const baseURL = 'http://localhost:3030/jsonstore/advanced/profiles';

    const profileCardsResponse = await fetch(baseURL);
    const profileCards = await profileCardsResponse.json();

    const mainElement = document.getElementById('main')
    mainElement.innerHTML = '';

    let counter = 1;

    for (let [profileID, profileInfo] of Object.entries(profileCards)) {
        const divProfileElement = document.createElement('div');
        divProfileElement.className = 'profile';

        divProfileElement.innerHTML = `
            <img src="./iconProfile2.png" class="userIcon" />
            <label>Lock</label>
            <input type="radio" name="user${counter}Locked" value="lock" checked>
            <label>Unlock</label>
            <input type="radio" name="user${counter}Locked" value="unlock"><br>
            <hr>
            <label>Username</label>
            <input type="text" name="user${counter}Username" value="${profileInfo.username}" disabled readonly />
            <div class="user${counter}HiddenFields">
                <hr>
                <label>Email:</label>
                <input type="email" name="user${counter}Email" value="${profileInfo.email}" disabled readonly />
                <label>Age:</label>
                <input type="email" name="user${counter}Age" value="${profileInfo.age}" disabled readonly />
                </div>
                
                <button>Show more</button>
        `
        divProfileElement.querySelector('div').style.display = 'none';

        mainElement.appendChild(divProfileElement);

        const showMoreButton = divProfileElement.querySelector('button');
        showMoreButton.addEventListener('click', showMoreButtonFunctionality);

        function showMoreButtonFunctionality() {
            const lockedRadioButton = divProfileElement.querySelector('input[type=radio]');

            if (!lockedRadioButton.checked && showMoreButton.textContent === 'Show more') {
                showMoreButton.textContent = 'Hide it';
                divProfileElement.querySelector('div').style.display = 'block';
            } else if (!lockedRadioButton.checked && showMoreButton.textContent === 'Hide it') {
                showMoreButton.textContent = 'Show more';
                divProfileElement.querySelector('div').style.display = 'none';
            }
        }

        counter++;
    }
}