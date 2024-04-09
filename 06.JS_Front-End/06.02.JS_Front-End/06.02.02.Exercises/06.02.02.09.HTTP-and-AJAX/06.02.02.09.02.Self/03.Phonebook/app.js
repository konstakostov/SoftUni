function attachEvents() {
    const baseURL = 'http://localhost:3030/jsonstore/phonebook';

    const loadButton = document.getElementById('btnLoad');
    loadButton.addEventListener('click', loadButtonFunctionality);

    const createButton = document.getElementById('btnCreate');
    createButton.addEventListener('click', createButtonFunctionality);

    const phonebookList = document.getElementById('phonebook');

    async function loadButtonFunctionality() {
        phonebookList.innerHTML = '';

        const phonesFetch = await fetch(baseURL);
        const phones = await phonesFetch.json();

        Object
            .entries(phones)
            .forEach(phone => {
                const phoneObject = phone[1];

                const deleteButton = document.createElement('button');
                deleteButton.textContent = 'Delete';
                deleteButton.addEventListener('click', deleteButtonFunctionality)

                const liElement = document.createElement('li');
                liElement.textContent = `${phoneObject.person}: ${phoneObject.phone}`;
                liElement.appendChild(deleteButton);

                phonebookList.appendChild(liElement);

                function deleteButtonFunctionality() {
                    fetch(baseURL + `/${phoneObject._id}`, {
                        method: 'DELETE'
                    });

                    liElement.remove();
                }
            })
    }

    function createButtonFunctionality() {
        const person = document.getElementById('person');
        const phone = document.getElementById('phone');

        const createPhoneObject = {
            person: person.value,
            phone: phone.value,
        }

        fetch(baseURL, {
            method: 'POST',
            body: JSON.stringify(createPhoneObject),
        })

        person.value = '';
        phone.value = '';

        loadButtonFunctionality();
    }
}

attachEvents();