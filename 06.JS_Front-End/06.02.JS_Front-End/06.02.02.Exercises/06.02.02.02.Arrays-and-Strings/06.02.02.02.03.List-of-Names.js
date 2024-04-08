function solve(namesArray) {
    let orderedNames = namesArray.sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));

    orderedNames.forEach((name, index) => {
        console.log(`${index + 1}.${name}`);
    })
}

solve(["John", "Bob", "Christina", "Ema"])
