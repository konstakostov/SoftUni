function solve(inputData) {
    let horses = inputData.splice(0, 1)[0].split('|');

    for (const line of inputData) {
        if (line === 'Finish') {
            const horsesDescending = horses.reverse();

            console.log(horsesDescending.join('->'));
            console.log(`The winner is: ${horsesDescending[horsesDescending.length - 1]}`)

            break;
        }

        if (line.startsWith('Retake')) {
            const [, overtaking, overtaken] = line.split(' ');

            const indexTaking = horses.indexOf(overtaking);
            const indexTaken = horses.indexOf(overtaken);

            if (indexTaking < indexTaken) {
                [horses[indexTaking], horses[indexTaken]] = [horses[indexTaken], horses[indexTaking]];
                console.log(`${overtaking} retakes ${overtaken}.`);
            }
        } else if (line.startsWith('Trouble')) {
            const [, name] = line.split(' ');

            const indexHorse = horses.indexOf(name);

            if (indexHorse > 0) {
                [horses[indexHorse], horses[indexHorse - 1]] = [horses[indexHorse - 1], horses[indexHorse]];
                console.log(`Trouble for ${name} - drops one position.`)
            }
        } else if (line.startsWith('Rage')) {
            const [, name] = line.split(' ');

            const indexHorse = horses.indexOf(name);

            if (indexHorse === horses.length - 2) {
                [horses[indexHorse], horses[indexHorse + 1]] = [horses[indexHorse + 1], horses[indexHorse]];
            } else if (indexHorse < horses.length - 2) {
                [horses[indexHorse], horses[indexHorse + 2]] = [horses[indexHorse + 2], horses[indexHorse]];
            }
            console.log(`${name} rages 2 positions ahead.`)
        } else if (line === 'Miracle') {
            const miracleHorse = horses.shift();
            horses.push(miracleHorse);
            console.log(`What a miracle - ${miracleHorse} becomes first.`)
        }
    }
}


solve((['Bella|Alexia|Sugar',
    'Retake Alexia Sugar',
    'Rage Bella',
    'Trouble Bella',
    'Finish']));

console.log();

solve((['Onyx|Domino|Sugar|Fiona',
    'Trouble Onyx',
    'Retake Onyx Sugar',
    'Rage Domino',
    'Miracle',
    'Finish']));

console.log();

solve((['Fancy|Lilly',
    'Retake Lilly Fancy',
    'Trouble Lilly',
    'Trouble Lilly',
    'Finish',
    'Rage Lilly']));