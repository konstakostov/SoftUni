// // Solution 01
// function colorize() {
//     const evenRowElements = document.querySelectorAll('table tr:nth-child(2n)');
//
//     for (const row of evenRowElements) {
//         row.style.background = 'teal';
//     }
//
//     // // Judge won't recognize this row;
//     // evenRowElements.forEach(row => row.style.background = 'teal');
// }

// Solution 02
function colorize() {
    let rows = document.querySelectorAll("table tr");
    let index = 0;
    for (let row of rows) {
        index++;
        if (index % 2 === 0)
            row.style.background = "teal";
    }
}
