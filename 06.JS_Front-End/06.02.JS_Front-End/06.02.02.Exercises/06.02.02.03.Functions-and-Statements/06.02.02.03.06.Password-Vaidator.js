function solve(inputPassword) {
    const messageValid = 'Password is valid';
    const messageLength = 'Password must be between 6 and 10 characters';
    const messageCharacters = 'Password must consist only of letters and digits';
    const messageDigits = 'Password must have at least 2 digits';

    const isLength = passwordLength(inputPassword);
    const isCharacters = passwordCharacters(inputPassword);
    const isDigits = passwordDigits(inputPassword) >= 2;

    function passwordLength(password) {
        return password.length >= 6 && password.length <= 10;
    }

    function passwordCharacters(password) {
        const pattern = /^[a-zA-Z0-9]+$/;

        return pattern.test(password);
    }

    function passwordDigits(password) {
        let counter = 0;

        for (let char of password) {
            if (!isNaN(parseInt(char, ))) {
                counter++;
            }
        }

        return counter;
    }

    if (isLength === true && isCharacters === true && isDigits === true) {
        console.log(messageValid);
    } else {
        if (!isLength) {
            console.log(messageLength);
        }
        if (!isCharacters) {
            console.log(messageCharacters);
        }
        if (!isDigits) {
            console.log(messageDigits);
        }
    }
}

solve('logIn');
solve('MyPass123');
solve('Pa$s$s');




