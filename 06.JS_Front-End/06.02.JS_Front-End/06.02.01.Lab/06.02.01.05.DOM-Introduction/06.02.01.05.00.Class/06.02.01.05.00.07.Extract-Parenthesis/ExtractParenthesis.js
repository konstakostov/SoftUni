// // Solution 01
// function extract(content) {
//     const contentElement = document.getElementById('content');
//
//     const matches = contentElement.textContent.matchAll(/\(([^)]+)\)/g);
//
//     const text = Array
//         .from(matches)
//         .map(match => match[1])
//         .join(';');
//
//     return text;
// }

// Solution 01
function extract(content) {
    let parameterElements = document.getElementById(content).textContent;
    let pattern = /\(([^)]+)\)/g;

    let result = [];
    let match = pattern.exec(parameterElements);

    while (match) {
        result.push(match[1]);
        match = pattern.exec(parameterElements);
    }

    return result.join('; ');
}