function solve(inputString) {
    let stringArray = inputString.split(' ');
    let specialWords = [];

    const pattern = /^#[a-zA-Z]+$/;

    stringArray.forEach(word => {
        if (pattern.test(word)) {
            specialWords.push(word.substring(1));
        }
    })

    console.log(specialWords.join('\n'))
}

solve('Nowadays everyone uses # to tag a #special word in #socialMedia');
solve('The symbol # is known #variously in English-speaking #regions as the #number sign');
