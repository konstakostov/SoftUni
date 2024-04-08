function sumTable() {
    const productCostElements = document.querySelectorAll('tr td:last-of-type:not(#sum)');
    const totalSumElement = document.getElementById('sum');


    totalSumElement.textContent = Array
        .from(productCostElements)
        .reduce((sum, element) => sum + Number(element.textContent), 0);
}