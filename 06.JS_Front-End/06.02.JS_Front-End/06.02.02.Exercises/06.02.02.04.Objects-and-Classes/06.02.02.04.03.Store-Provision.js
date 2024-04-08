function solve(inputStock, inputOrders) {
    let stock = {}

    for (let i = 0; i < inputStock.length; i += 2) {
        stock[inputStock[i]] = Number(inputStock[i + 1]);
    }

    for (let j = 0; j < inputOrders.length; j += 2) {
        if (Object.keys(stock).includes(inputOrders[j])) {
            stock[inputOrders[j]] += Number(inputOrders[j + 1]);
        } else {
            stock[inputOrders[j]] = Number(inputOrders[j + 1]);
        }
    }

    Object.keys(stock).forEach(product => console.log(`${product} -> ${stock[product]}`))
}

solve(
    [
        'Chips', '5', 'CocaCola', '9', 'Bananas', '14', 'Pasta', '4', 'Beer', '2'
    ],
    [
        'Flour', '44', 'Oil', '12', 'Pasta', '7', 'Tomatoes', '70', 'Bananas', '30'
    ]
);
solve(
    [
        'Salt', '2', 'Fanta', '4', 'Apple', '14', 'Water', '4', 'Juice', '5'
    ],
    [
        'Sugar', '44', 'Oil', '12', 'Apple', '7', 'Tomatoes', '7', 'Bananas', '30'
    ]
);