// // Solution 01;
// function extractText() {
//     const itemElements = document.getElementById('items');
//     const textAreaElement = document.getElementById('result');
//
//     textAreaElement.value = itemElements.textContent;
// }

// Solution 02;
function extractText() {
    let itemNodes = document.querySelectorAll("ul#items li");
    let textArea = document.querySelector("#result");

    for (let node of itemNodes) {
        textArea.value += node.textContent.trim() + '\n'
    }
}