function solve(inputString) {
    let person = JSON.parse(inputString);

    Object
        .keys(person)
        .forEach(property => console.log(`${property}: ${person[property]}`));
}

solve('{"name": "George", "age": 40, "town": "Sofia"}');
solve('{"name": "Peter", "age": 35, "town": "Plovdiv"}');