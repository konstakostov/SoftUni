function solve(fruit, grams, pricePerKg) {
    const kilograms = grams / 1000;
    const money = kilograms * pricePerKg

    console.log(`I need $${money.toFixed(2)} to buy ${kilograms.toFixed(2)} kilograms ${fruit}.`)
}

solve('orange', 2500, 1.80);
solve('apple', 1563, 2.35);