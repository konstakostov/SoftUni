function solve() {
    const textAreaInputElement = document.querySelector('#exercise textarea:first-of-type');
    const textAreaOutputElement = document.querySelector('#exercise textarea:last-of-type');
    const generateButtonElement = document.querySelector('#exercise button:first-of-type');
    const buyButtonElement = document.querySelector('#exercise button:last-of-type');
    const furnitureTbodyElement = document.querySelector('.table tbody');

    // Parse input when the 'Generate' Button is pressed;
    generateButtonElement.addEventListener('click', (e) => {
        const inputData = JSON.parse(textAreaInputElement.value);

        for (const furniture of inputData) {
            // Create an img and td element & Append the img element to the td element;
            const imgElement = document.createElement('img');
            imgElement.src = furniture.img;
            const imgTdElement = document.createElement('td');
            imgTdElement.appendChild(imgElement);

            // Create a pName and td element & Append the pName element to the td element;
            const pNameElement = document.createElement('p');
            pNameElement.textContent = furniture.name;
            const pNameTdElement = document.createElement('td');
            pNameTdElement.appendChild(pNameElement);

            // Create a pPrice and td element & Append the pPrice element to the td element;
            const pPriceElement = document.createElement('p');
            pPriceElement.textContent = furniture.price;
            const pPriceTdElement = document.createElement('td');
            pPriceTdElement.appendChild(pPriceElement);

            // Create a pDecFactor and td element & Append the pDecFactor element to the td element;
            const pDecFactorElement = document.createElement('p');
            pDecFactorElement.textContent = furniture.decFactor;
            const pDecFactorTdElement = document.createElement('td');
            pDecFactorTdElement.appendChild(pDecFactorElement);

            // Create a checkbox and td element & Append the checkbox element to the td element;
            const checkboxElement = document.createElement('input');
            checkboxElement.setAttribute('type', 'checkbox');
            const markTdElement = document.createElement('td');
            markTdElement.appendChild(checkboxElement);

            // Create a tr element & Append all td elements to it;
            const  furnitureTrElement = document.createElement('tr');
            furnitureTrElement.appendChild(imgTdElement);
            furnitureTrElement.appendChild(pNameTdElement);
            furnitureTrElement.appendChild(pPriceTdElement);
            furnitureTrElement.appendChild(pDecFactorTdElement);
            furnitureTrElement.appendChild(markTdElement);

            // Append the tr element to the tBody element;
            furnitureTbodyElement.appendChild(furnitureTrElement);
        }
    })

    // Display result when the 'Buy' button is pressed;
    buyButtonElement.addEventListener('click', (e) => {
        textAreaOutputElement.textContent = '';

        let totalPrice = 0;
        let totalDecFactor = 0;
        let markedChildren = 0;
        let names = [];

        Array
            .from(furnitureTbodyElement.children)
            .forEach(furnitureTrElement => {
                const markInputElement = furnitureTrElement.querySelector('input[type=checkbox]');

                if (!markInputElement.checked) {
                    return;
                }
                const name = furnitureTrElement.children.item(1).textContent;
                const price = Number(furnitureTrElement.children.item(2).textContent);
                const decFactor = Number(furnitureTrElement.children.item(3).textContent);

                names.push(name);
                totalPrice += price;
                totalDecFactor += decFactor;
                markedChildren++;
            })

        const averageDecFactor = totalDecFactor / markedChildren;

        textAreaOutputElement.textContent += `Bought furniture: ${names.join(', ')}\n`;
        textAreaOutputElement.textContent += `Total price: ${totalPrice.toFixed(2)}\n`;
        textAreaOutputElement.textContent += `Average decoration factor: ${averageDecFactor}`;
    })
}