// Solution 01
function sumTable() {
    const tdCostElements = document.querySelectorAll('tr td:last-of-type:not(#sum)');
    const tdSumElements = document.getElementById("sum");

    tdSumElements.textContent = Array
        .from(tdCostElements)
        .reduce((sum, element) => sum + Number(element.textContent), 0);
}

// // Solution 02
// function sumTable() {
//     let table = document.querySelectorAll("table tr");
//     let total = 0;
//     for (let i = 1; i < table.length; i++) {
//         let cols = table[i].children;
//         let cost = cols[cols.length - 1].textContent;
//         total += Number(cost);
//     }
//     document.getElementById("sum").textContent = total;
// }