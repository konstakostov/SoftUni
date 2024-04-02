function solve(inputArray) {
    let towns = [];

    inputArray.forEach(line => {
        const [town, latitude, longitude] = line.split(' | ')
        const townsData = {
            town: town,
            latitude: Number(latitude).toFixed(2).toString(),
            longitude: Number(longitude).toFixed(2).toString(),
        };

        towns.push(townsData);
    });

    towns.forEach(town => {console.log(town)})
}

solve(['Sofia | 42.696552 | 23.32601', 'Beijing | 39.913818 | 116.363625']);
solve(['Plovdiv | 136.45 | 812.575']);