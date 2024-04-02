function solve(inputArray) {
    let garage = {};

    for (const line of inputArray) {
        const [command, plate] = line.split(', ');

        if (command === 'IN') {
            garage[plate] = true;
        } else if (command === 'OUT' && garage[plate]) {
            delete garage[plate];
        }
    }

    if (Object.keys(garage).length > 0) {
        Object
            .keys(garage)
            .sort((a, b) => a.localeCompare(b))
            .forEach(car => console.log(car));
    } else {
        console.log('Parking Lot is Empty')
    }
}

solve(
    [
        'IN, CA2844AA',
        'IN, CA1234TA',
        'OUT, CA2844AA',
        'IN, CA9999TT',
        'IN, CA2866HI',
        'OUT, CA1234TA',
        'IN, CA2844AA',
        'OUT, CA2866HI',
        'IN, CA9876HH',
        'IN, CA2822UU'
    ]
);
solve(
    [
        'IN, CA2844AA',
        'IN, CA1234TA',
        'OUT, CA2844AA',
        'OUT, CA1234TA'
    ]
);