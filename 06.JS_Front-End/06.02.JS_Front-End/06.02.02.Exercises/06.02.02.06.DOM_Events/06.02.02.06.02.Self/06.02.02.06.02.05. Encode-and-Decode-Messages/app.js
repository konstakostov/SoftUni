function encodeAndDecodeMessages() {
    const buttonElements = document.querySelectorAll("button");
    const encodeButtonElement = buttonElements[0];
    const decodeButtonElement = buttonElements[1];

    const textAreaElements = document.querySelectorAll("textarea");
    const encodeTextElement = textAreaElements[0];
    const decodeTextElement = textAreaElements[1];

    encodeButtonElement.addEventListener('click', () => {
        const messageToEncode = encodeTextElement.value;
        let encodedMessage = ''

        for (let i = 0; i < messageToEncode.length; i++) {
            const charToAscii = messageToEncode.charCodeAt(i);

            encodedMessage += String.fromCharCode(charToAscii + 1);
        }

        encodeTextElement.value = '';
        decodeTextElement.value = encodedMessage;
    })

    decodeButtonElement.addEventListener('click', () => {
        const messageToDecode = decodeTextElement.value;
        let decodedMessage = '';

        for (let i = 0; i < messageToDecode.length; i++) {
            const charToAscii = messageToDecode.charCodeAt(i);

            decodedMessage += String.fromCharCode(charToAscii - 1);
        }

        encodeTextElement.value = decodedMessage;
        decodeTextElement.value = '';
    })
}