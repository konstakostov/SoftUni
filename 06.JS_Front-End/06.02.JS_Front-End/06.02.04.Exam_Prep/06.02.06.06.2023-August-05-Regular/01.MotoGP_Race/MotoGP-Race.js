function solve(inputData) {
    const numRiders = inputData.splice(0, 1);

    let riders = {};

    for (const data of inputData.splice(0, numRiders)) {
        const [name, fuel, position] = data.split('|');

        riders[name] = {
            fuel: Number(fuel),
            position: Number(position),
        };
    }

    for (let line of inputData) {
        if (line === 'Finish') {
            Object
                .keys(riders)
                .forEach(name => {
                    console.log(`${name}`);
                    console.log(`  Final position: ${riders[name].position}`)
                });

            break;
        } else if (line.startsWith('StopForFuel')) {
            const [command, name, minFuel, newPosition] = line.split(' - ');

            if (riders[name].fuel < Number(minFuel)) {
                riders[name].position = Number(newPosition);
                console.log(`${name} stopped to refuel but lost his position, now he is ${Number(newPosition)}.`)
            } else {
                console.log(`${name} does not need to stop for fuel!`)
            }
        } else if (line.startsWith('Overtaking')) {
            const [command, rider01, rider02] = line.split(' - ');

            const rider01Position = riders[rider01].position;
            const rider02Position = riders[rider02].position;

            if (rider01Position < rider02Position) {
                riders[rider01].position = rider02Position;
                riders[rider02].position = rider01Position;

                console.log(`${rider01} overtook ${rider02}!`)
            }
        } else if (line.startsWith('EngineFail')) {
            const [command, rider, laps] = line.split(' - ');
                delete riders[rider];
                console.log(`${rider} is out of the race because of a technical issue, ${laps} laps before the finish.`)
        }
    }
}

solve((
    [
        "3",
        "Valentino Rossi|100|1",
        "Marc Marquez|90|2",
        "Jorge Lorenzo|80|3",
        "StopForFuel - Valentino Rossi - 50 - 1",
        "Overtaking - Marc Marquez - Jorge Lorenzo",
        "EngineFail - Marc Marquez - 10",
        "Finish"
    ])
);

console.log();

solve((
    [
        "4",
        "Valentino Rossi|100|1",
        "Marc Marquez|90|3",
        "Jorge Lorenzo|80|4",
        "Johann Zarco|80|2",
        "StopForFuel - Johann Zarco - 90 - 5",
        "Overtaking - Marc Marquez - Jorge Lorenzo",
        "EngineFail - Marc Marquez - 10",
        "Finish"
    ])
);