function solve(inputArray) {
    let employees = {}

    inputArray.forEach(employee => {
        employees[employee] = employee.length;
    })

    Object
        .keys(employees)
        .forEach(employee => console.log(`Name: ${employee} -- Personal Number: ${employees[employee]}`))
}

solve(
    [
        'Silas Butler',
        'Adnaan Buckley',
        'Juan Peterson',
        'Brendan Villarreal'
    ]
);
solve(
    [
        'Samuel Jackson',
        'Will Smith',
        'Bruce Willis',
        'Tom Holland'
    ]
);