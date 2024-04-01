function solve(item, quantity) {
    const coffeePrice = 1.50;
    const waterPrice = 1.00;
    const cokePrice = 1.40;
    const snacksPrice = 2.00;

    let finalPrice = 0;

    switch (item) {
        case 'coffee':
            finalPrice += quantity * coffeePrice;
            break;
        case 'water':
            finalPrice += quantity * waterPrice;
            break;
        case 'coke':
            finalPrice += quantity * cokePrice;
            break;
        case 'snacks':
            finalPrice += quantity * snacksPrice;
            break;
    }

    console.log(finalPrice.toFixed(2));
}

solve("water", 5);
solve("coffee", 2);
