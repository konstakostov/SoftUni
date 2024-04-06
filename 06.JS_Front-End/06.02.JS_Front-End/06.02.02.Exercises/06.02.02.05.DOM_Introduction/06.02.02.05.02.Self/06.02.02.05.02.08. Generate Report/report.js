function generateReport() {
    const resultElement = document.getElementById('output');
    const tableHeadElements = document.querySelectorAll('table thead th');
    const tableDataElements = document.querySelectorAll('table tbody tr');

    const activeColumns = Array
        .from(tableHeadElements)
        .map((thElement) => {
            const checkboxElement = thElement.querySelector('input[type=checkbox]');

            return {
                name: thElement.textContent.toLowerCase().trim(),
                isActive: checkboxElement.checked,
            }
        })

    const reportData = Array
        .from(tableDataElements)
        .map((trElement) => {
            const cellElement = trElement.querySelectorAll('td');

            return Array
                .from(cellElement)
                .reduce((data, cell, i) => {
                    if (!activeColumns[i].isActive) {
                        return data;
                    }

                    const columnName = activeColumns[i].name;
                    data[columnName] = cell.textContent;

                    return data;
                }, {});
        })

    resultElement.value = JSON.stringify(reportData, null, 2);
}