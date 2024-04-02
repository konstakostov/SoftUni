function solve(city) {
    Object
        .keys(city)
        .forEach(property => console.log(`${property} -> ${city[property]}`))
}

solve(
    {
        name: "Sofia",
        area: 492,
        population: 1238438,
        country: "Bulgaria",
        postCode: "1000"
    }
);
solve(
    {
        name: "Plovdiv",
        area: 389,
        population: 1162358,
        country: "Bulgaria",
        postCode: "4000"
    }
);