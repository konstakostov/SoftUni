function solve(size) {
    let matrix = [];

    for (let i = 0; i < size; i++) {
        let row = [];

        for (let j = 0; j < size; j++) {
            row.push(size);
        }

        matrix.push(row);
    }

    for (let i = 0; i < size; i++) {
        console.log(matrix[i].join(' '));
    }
}

solve(3);
solve(7);
solve(2);