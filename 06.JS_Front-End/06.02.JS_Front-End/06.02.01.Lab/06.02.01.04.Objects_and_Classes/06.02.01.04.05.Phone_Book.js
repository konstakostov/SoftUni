function solve(inputArray) {
    let phoneBook = {};

    for (const line of inputArray) {
        const [name, phone] = line.split(' ');
        phoneBook[name] = phone;
    }

    Object
        .keys(phoneBook)
        .forEach(name => console.log(`${name} -> ${phoneBook[name]}`))
}

solve(
    [
        'Tim 0834212554',
        'Peter 0877547887',
        'Bill 0896543112',
        'Tim 0876566344'
    ]
);
solve(
    [
        'George 0552554',
        'Peter 087587',
        'George 0453112',
        'Bill 0845344'
    ]
);