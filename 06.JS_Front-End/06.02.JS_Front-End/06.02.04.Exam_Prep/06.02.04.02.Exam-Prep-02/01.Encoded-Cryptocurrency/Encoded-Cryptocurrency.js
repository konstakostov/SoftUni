function solve(inputArray) {
    let message = inputArray.splice(0, 1).toString();

    for (const line of inputArray) {
        if (line === 'Buy') {
            console.log(`The cryptocurrency is: ${message}`);

            break;
        } else if (line === 'TakeEven') {
            let newMessage = '';

            for (let i = 0; i < message.length; i += 2) {
                newMessage += message[i];
            }

            message = newMessage;

            console.log(message);
        } else if (line.startsWith('ChangeAll')) {
            const [_, substring, replacement] = line.split('?');

            message = message.split(substring).join(replacement);
            console.log(message);
        } else if (line.startsWith('Reverse')) {
            const substring = line.replace('Reverse?', '');

            if (message.includes(substring)) {
                const reverseSubstring = substring.split('').reverse().join('');

                const messageLeft = message.slice(0, message.indexOf(substring));
                const messageRight = message.slice(message.indexOf(substring) + substring.length);

                message = messageLeft + messageRight + reverseSubstring;

                console.log(message)
            } else {
                console.log('error');
            }
        }
    }
}

solve(([
    "z2tdsfndoctsB6z7tjc8ojzdngzhtjsyVjek!snfzsafhscs",
    "TakeEven",
    "Reverse?!nzahc",
    "ChangeAll?m?g",
    "Reverse?adshk",
    "ChangeAll?z?i",
    "Buy"
]));

solve(([
    "PZDfA2PkAsakhnefZ7aZ",
    "TakeEven",
    "TakeEven",
    "TakeEven",
    "ChangeAll?Z?X",
    "ChangeAll?A?R",
    "Reverse?PRX",
    "Buy"
]));