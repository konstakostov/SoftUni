function colorize() {
    const tableRows = document.querySelectorAll('table tr');

    let rowIndex = 1;

    for (const row of tableRows) {
        if (rowIndex % 2 === 0) {
            row.style.background = 'Teal';
        }

        rowIndex += 1;
    }
}