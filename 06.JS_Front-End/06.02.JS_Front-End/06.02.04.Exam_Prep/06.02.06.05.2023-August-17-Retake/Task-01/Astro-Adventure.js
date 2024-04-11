function solve(inputData) {
    const numAstronauts = inputData.splice(0, 1);

    const minEnergy = 0;
    const maxEnergy = 200;

    const minOxygen = 0;
    const maxOxygen = 100;

    let astronauts = {};

    for (const data of inputData.splice(0, numAstronauts)) {
        const [name, oxygen, energy] = data.split(' ');

        astronauts[name] = {
            oxygen: Number(oxygen),
            energy: Number(energy),
        }
    }

    for (const line of inputData) {
        const [command, name, resourceString] = line.split(' - ');

        const resource = Number(resourceString);

        if (command === 'Explore') {
            let currentEnergy = astronauts[name].energy;

            if (currentEnergy < resource) {
                console.log(`${name} does not have enough energy to explore!`)
            } else {
                astronauts[name].energy -= resource;
                currentEnergy = astronauts[name].energy
                console.log(`${name} has successfully explored a new area and now has ${currentEnergy} energy!`)
            }
        } else if (command === 'Refuel') {
            let currentEnergy = astronauts[name].energy;
            let amountIncreased = 0

            if (currentEnergy + resource > maxEnergy) {
                amountIncreased = maxEnergy - currentEnergy;
                astronauts[name].energy = maxEnergy;
            } else {
                amountIncreased = resource;
                astronauts[name].energy += resource;
            }

            console.log(`${name} refueled their energy by ${amountIncreased}!`);
        } else if (command === 'Breathe') {
            let currentOxygen = astronauts[name].oxygen;
            let amountIncreased = 0;

            if (currentOxygen + resource > maxOxygen) {
                amountIncreased = maxOxygen - currentOxygen;
                astronauts[name].oxygen = maxOxygen;
            } else {
                amountIncreased = resource;
                astronauts[name].oxygen += resource;
            }

            console.log(`${name} took a breath and recovered ${amountIncreased} oxygen!`);
        }
    }

    Object
        .keys(astronauts)
        .forEach(name => {
            console.log(`Astronaut: ${name}, Oxygen: ${astronauts[name].oxygen}, Energy: ${astronauts[name].energy}`)
        })
}

solve([
    '3',
    'John 50 120',
    'Kate 80 180',
    'Rob 70 150',
    'Explore - John - 50',
    'Refuel - Kate - 30',
    'Breathe - Rob - 20',
    'End'
]);

console.log();

solve([
    '4',
    'Alice 60 100',
    'Bob 40 80',
    'Charlie 70 150',
    'Dave 80 180',
    'Explore - Bob - 60',
    'Refuel - Alice - 30',
    'Breathe - Charlie - 50',
    'Refuel - Dave - 40',
    'Explore - Bob - 40',
    'Breathe - Charlie - 30',
    'Explore - Alice - 40',
    'End'
]);
