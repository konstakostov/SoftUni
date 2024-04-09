function attachEvents() {
    const requestURL = 'http://localhost:3030/jsonstore/messenger';

    const sendButton = document.getElementById('submit');
    const refreshButton = document.getElementById('refresh');

    const textElement = document.getElementById('messages');



    sendButton.addEventListener('click', sendButtonFunctionality);
    refreshButton.addEventListener('click', refreshButtonFunctionality);

    function sendButtonFunctionality() {
        const author = document.getElementsByName('author')[0].value;
        const content = document.getElementsByName('content')[0].value;

        fetch(requestURL, {
            method: 'POST',
            headers: {
                'content-type': 'application/json'
            },
            body: JSON.stringify({
                author,
                content,
            })
        })
    }

    async function refreshButtonFunctionality() {
        textElement.textContent = '';

        const messagesRefresh = await fetch(requestURL);
        const messages = await messagesRefresh.json();

        let messagesArray = [];

        Object
            .entries(messages)
            .forEach(currMessage => {
                messagesArray.push(`${currMessage[1].author}: ${currMessage[1].content}`);
            });

        textElement.textContent = messagesArray.join('\n');
    }
}

attachEvents();