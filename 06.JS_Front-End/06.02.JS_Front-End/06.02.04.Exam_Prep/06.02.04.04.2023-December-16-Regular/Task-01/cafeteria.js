function solve(input) {
    const numBaristas = Number(input.splice(0, 1));
    const baristasData = input.splice(0, numBaristas);

    let baristas = {};

    for (const current of baristasData) {
        const [name, shift, coffees] = current.split(' ');

        baristas[name] = {
            shift: shift,
            coffeeTypes: coffees.split(','),
        }
    }

    for (const line of input) {
        if (line.startsWith('Prepare')) {
            const [name, shift, coffee] = line.replace('Prepare / ', '').split(' / ');

            if (baristas[name].shift === shift && baristas[name].coffeeTypes.includes(coffee)) {
                console.log(`${name} has prepared a ${coffee} for you!`)
            } else {
                console.log(`${name} is not available to prepare a ${coffee}.`)
            }
        } else if (line.startsWith('Change Shift')) {
            const [name, shift] = line.replace('Change Shift / ', '').split(' / ');

            baristas[name].shift = shift;

            console.log(`${name} has updated his shift to: ${shift}`);
        } else if (line.startsWith('Learn')) {
            const [name, coffee] = line.replace('Learn / ', '').split(' / ');

            if (baristas[name].coffeeTypes.includes(coffee)) {
                console.log(`${name} knows how to make ${coffee}.`)
            } else {
                baristas[name].coffeeTypes.push(coffee);

                console.log(`${name} has learned a new coffee type: ${coffee}.`)
            }
        }
    }

    Object
        .keys(baristas)
        .forEach(name => {
            console.log(`Barista: ${name}, Shift: ${baristas[name].shift}, Drinks: ${baristas[name].coffeeTypes.join(', ')}`)
    })
}

solve(
    [
        '3',
        'Alice day Espresso,Cappuccino',
        'Bob night Latte,Mocha',
        'Carol day Americano,Mocha',
        'Prepare / Alice / day / Espresso',
        'Change Shift / Bob / night',
        'Learn / Carol / Latte',
        'Learn / Bob / Latte',
        'Prepare / Bob / night / Latte',
        'Closed'
    ]
);
solve(
    [
        '4',
        'Alice day Espresso,Cappuccino',
        'Bob night Latte,Mocha',
        'Carol day Americano,Mocha',
        'David night Espresso',
        'Prepare / Alice / day / Espresso',
        'Change Shift / Bob / day',
        'Learn / Carol / Latte',
        'Prepare / Bob / night / Latte',
        'Learn / David / Cappuccino',
        'Prepare / Carol / day / Cappuccino',
        'Change Shift / Alice / night',
        'Learn / Bob / Mocha',
        'Prepare / David / night / Espresso',
        'Closed'
    ]
);