function solve(x, y) {
    let allCharacters = [];
    let char01;
    let char02;

    if (x.charCodeAt(0) < y.charCodeAt(0)) {
        char01 = x.charCodeAt(0);
        char02 = y.charCodeAt(0);
    } else {
        char01 = y.charCodeAt(0);
        char02 = x.charCodeAt(0);
    }

    for (let i = char01 + 1; i < char02; i++) {
        allCharacters.push(String.fromCharCode(i));
    }

    console.log(allCharacters.join(' '))
}

solve('a', 'd');
solve('#', ':');
solve('C', '#');
