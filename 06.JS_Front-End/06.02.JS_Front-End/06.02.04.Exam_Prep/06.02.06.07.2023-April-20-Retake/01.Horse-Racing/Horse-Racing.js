function solve(inputData) {
    const horsesInput = inputData.splice(0, 1)[0];
    let horses = horsesInput.split('|');

    for (const line of inputData) {
        if (line === 'Finish') {
            break;
        } else if (line.startsWith('Retake')) {
            const [, overtaking, overtaken] = line.split(' ');

            const overtakingIndex = horses.indexOf(overtaking);
            const overtakenIndex = horses.indexOf(overtaken);

            const overtakingHorse = horses[overtakingIndex];
            const overtakenHorse = horses[overtakenIndex];

            if (overtakingIndex < overtakenIndex) {
                horses.splice(overtakenIndex, 1);
                horses.splice(overtakingIndex, 1);

                horses.splice(overtakingIndex, 0, overtakenHorse);
                horses.splice(overtakenIndex, 0, overtakingHorse);

                console.log(`${overtakingHorse} retakes ${overtakenHorse}.`);
            }
        } else if (line.startsWith('Trouble')) {
            const [, name] = line.split(' ');
            const horseIndex = horses.indexOf(name);
            const horseNewIndex = horseIndex - 1;

            if (horseIndex > 0) {
                horses.splice(horseIndex, 1);
                horses.splice(horseNewIndex, 0, name);

                console.log(`Trouble for ${name} - drops one position.`)
            }
        } else if (line.startsWith('Rage')) {
            const [, name] = line.split(' ');
            const horseIndex = horses.indexOf(name);
            const fistPositionIndex = horses.length - 1;
            const secondPositionIndex = fistPositionIndex - 1;


            if (horseIndex === secondPositionIndex) {
                horses.splice(horseIndex, 1);
                horses.splice(horseIndex + 1, 0, name);
            } else if (horseIndex < secondPositionIndex) {
                horses.splice(horseIndex, 1);
                horses.splice(horseIndex + 2, 0, name);
            }

            console.log(`${name} rages 2 positions ahead.`)
        } else if (line === 'Miracle') {
            const miracleHorse = horses.shift();
            horses.push(miracleHorse);

            console.log(`What a miracle - ${miracleHorse} becomes first.`)
        }
    }

    const lastHorseIndex = horses.length - 1;

    console.log(horses.join('->'))
    console.log(`The winner is: ${horses[lastHorseIndex]}`);
}


// Left                    -> Right
// Last                    -> First
// 0                       -> horses.length - 1
// Onyx -> Domino -> Sugar -> Fiona


solve(([
    'Bella|Alexia|Sugar',
    'Retake Alexia Sugar',
    'Rage Bella',
    'Trouble Bella',
    'Finish'
]));

console.log();

solve(([
    'Onyx|Domino|Sugar|Fiona',
    'Trouble Onyx',
    'Retake Onyx Sugar',
    'Rage Domino',
    'Miracle',
    'Finish'
]));

console.log();

solve(([
    'Fancy|Lilly',
    'Retake Lilly Fancy',
    'Trouble Lilly',
    'Trouble Lilly',
    'Finish',
    'Rage Lilly'
]));