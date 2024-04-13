window.addEventListener("load", solve);

function solve() {
    const nameInput = document.getElementById('name');
    const phoneInput = document.getElementById('phone');
    const categoryInput = document.getElementById('category');

    const checkList = document.getElementById('check-list');
    const contactList = document.getElementById('contact-list');

    const addButton = document.getElementById('add-btn');
    addButton.addEventListener('click', () => {
        const name = nameInput.value;
        const phone = phoneInput.value;
        const category = categoryInput.value;

        if (name !== '' && phone !== '' && category !== '') {
            // editButton;
            const editButton = document.createElement('button');
            editButton.classList.add('edit-btn');

            // saveButton;
            const saveButton = document.createElement('button');
            saveButton.classList.add('save-btn');

            // buttonContainer & Append buttons;
            const buttonContainer = document.createElement('div');
            buttonContainer.classList.add('buttons');
            buttonContainer.appendChild(editButton);
            buttonContainer.appendChild(saveButton);

            // pName;
            const pName = document.createElement('p');
            pName.textContent = `name:${name}`;

            // pPhone;
            const pPhone = document.createElement('p');
            pPhone.textContent = `phone:${phone}`;

            // pCategory;
            const pCategory = document.createElement('p');
            pCategory.textContent = `category:${category}`;

            // articleContainer;
            const articleContainer = document.createElement('article');
            articleContainer.appendChild(pName);
            articleContainer.appendChild(pPhone);
            articleContainer.appendChild(pCategory);

            // contactContainer;
            const contactContainer = document.createElement('li');
            contactContainer.appendChild(articleContainer);
            contactContainer.appendChild(buttonContainer);

            // Append contactContainer to checkList;
            checkList.appendChild(contactContainer);

            console.log(checkList)
            // Clear all input field values;
            nameInput.value = '';
            phoneInput.value = '';
            categoryInput.value = '';

            // editButton addEventListener
            editButton.addEventListener('click', () => {
                // Populate the input field values;
                nameInput.value = name;
                phoneInput.value = phone;
                categoryInput.value = category;

                // Remove contactContainer;
                contactContainer.remove();
            })

            // saveButton addEventListener
            saveButton.addEventListener('click', () => {
                // Remove buttonContainer and the buttons inside it;;
                buttonContainer.remove();

                // deleteButton;
                const deleteButton = document.createElement('button');
                deleteButton.className = 'del-btn';

                // Append deleteButton to contactContainer;
                contactContainer.appendChild(deleteButton);

                // Remove contactContainer from checkList
                checkList.removeChild(contactContainer);

                // Append contactContainer to contactList
                contactList.appendChild(contactContainer);

                // deleteButton addEventListener
                deleteButton.addEventListener('click', () => {
                    contactContainer.remove();
                })
            })
        }
    })
}