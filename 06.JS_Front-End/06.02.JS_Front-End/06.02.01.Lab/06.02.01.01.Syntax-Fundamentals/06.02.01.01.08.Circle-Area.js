function solve(radius) {
    let inputType = typeof(radius);

    if (inputType === 'number') {
        console.log((Math.PI * Math.pow(radius, 2)).toFixed(2));
    } else {
        console.log(`We can not calculate the circle area, because we receive a ${inputType}.`);
    }
}

solve(5);
solve('name');
