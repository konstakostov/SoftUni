function solve(inputText) {
    let text = inputText.shift();

    for (const command of inputText) {
        if (command === 'Buy') {
            console.log(`The cryptocurrency is: ${text}`)

            break;
        } else if (command === 'TakeEven') {
            let newText = ''

            for (let i = 0; i < text.length; i+= 2) {
                newText += text[i];
            }

            text = newText;
            console.log(text);
        } else if (command.startsWith('ChangeAll')) {
            const [usedCommand, substring, replacement] = command.split('?');

            text = text.split(substring).join(replacement);
            console.log(text);
        } else if (command.startsWith('Reverse')) {
            const [usedCommand, substring] = command.split('?');

            if (text.includes(substring)) {
                const reversedSubstring = substring.split('').reverse().join('');

                text = text.replace(substring, '') + reversedSubstring;
                console.log(text);
            } else {
                console.log('error')
            }
        }
    }
}

solve(
    (
        ["z2tdsfndoctsB6z7tjc8ojzdngzhtjsyVjek!snfzsafhscs",
            "TakeEven",
            "Reverse?!nzahc",
            "ChangeAll?m?g",
            "Reverse?adshk",
            "ChangeAll?z?i",
            "Buy"]
    )
);
solve(
    (
        ["PZDfA2PkAsakhnefZ7aZ",
            "TakeEven",
            "TakeEven",
            "TakeEven",
            "ChangeAll?Z?X",
            "ChangeAll?A?R",
            "Reverse?PRX",
            "Buy"]
    )
);
