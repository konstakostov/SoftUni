function solve(inputArray) {
    let addressBook = {};

    for (const line of inputArray) {
        const [name, address] = line.split(':')

        addressBook[name] = address;
    }

    Object
        .keys(addressBook)
        .sort()
        .forEach(name => console.log(`${name} -> ${addressBook[name]}`));
}

solve(
    [
        'Tim:Doe Crossing',
        'Bill:Nelson Place',
        'Peter:Carlyle Ave',
        'Bill:Ornery Rd'
    ]
);
solve(
    [
        'Bob:Huxley Rd',
        'John:Milwaukee Crossing',
        'Peter:Fordem Ave',
        'Bob:Redwing Ave',
        'George:Mesta Crossing',
        'Ted:Gateway Way',
        'Bill:Gateway Way',
        'John:Grover Rd',
        'Peter:Huxley Rd',
        'Jeff:Gateway Way',
        'Jeff:Huxley Rd'
    ]

);