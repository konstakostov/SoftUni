function solve(inputArray) {
    let meetings = {};

    for (const line of inputArray) {
        const [day, name] = line.split(' ');

        if (Object.keys(meetings).includes(day)) {
            console.log(`Conflict on ${day}!`);
        } else {
            meetings[day] = name;
            console.log(`Scheduled for ${day}`);
        }
    }

    Object.keys(meetings).forEach(day => console.log(`${day} -> ${meetings[day]}`))
}

solve(
    [
        'Monday Peter',
        'Wednesday Bill',
        'Monday Tim',
        'Friday Tim'
    ]
);
solve(
    [
        'Friday Bob',
        'Saturday Ted',
        'Monday Bill',
        'Monday John',
        'Wednesday George'
    ]
);