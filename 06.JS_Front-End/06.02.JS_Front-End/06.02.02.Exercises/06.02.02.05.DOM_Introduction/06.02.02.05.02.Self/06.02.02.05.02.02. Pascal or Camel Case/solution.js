function solve() {
    const inputText = document.getElementById('text').value;
    const inputConvention = document.getElementById('naming-convention').value;
    const result = document.getElementById('result');

    const convertToCamelCase = (inputString) => {
        const stringList = inputString.split(' ');
        let finalString = '';


        for (let i = 0; i < stringList.length; i++) {
            const word = stringList[i]

            if (i === 0) {
                finalString += word.toLowerCase();
            } else {
                finalString += word.charAt(0).toUpperCase() + word.slice(1).toLowerCase();
            }
        }

        return finalString;
    }

    const convertToPascalCase = (inputString) => {
        const stringList = inputString.split(' ');
        let finalString = '';

        for (let i = 0; i < stringList.length; i++) {
            finalString += stringList[i].charAt(0).toUpperCase() + stringList[i].slice(1).toLowerCase();
        }

        return finalString;
    }

    const convertor = {
        "Camel Case": convertToCamelCase,
        "Pascal Case": convertToPascalCase,
    }

    if (convertor[inputConvention]) {
        result.textContent = convertor[inputConvention](inputText);
    } else {
        result.textContent = 'Error!';
    }
}