function solve() {
    const addProductButtonElements = document.querySelectorAll('button.add-product');
    const textAreaElement = document.querySelector('textarea');
    const checkoutButtonElement = document.querySelector('button.checkout');

    let totalPrice = 0;
    let uniqueProducts = [];

    for (const buttonElement of addProductButtonElements) {
        const productElement = buttonElement.parentElement.parentElement;

        buttonElement.addEventListener('click', () => {
            const title = productElement.querySelector('.product-title').textContent;
            const price = productElement.querySelector('.product-line-price').textContent;

            totalPrice += Number(price);
            uniqueProducts[title] = true;

            textAreaElement.textContent += `Added ${title} for ${price} to the cart.\n`;
        })
    }

    checkoutButtonElement.addEventListener('click', (event) => {
        Array
            .from(addProductButtonElements)
            .forEach(buttonElement => buttonElement.setAttribute('disabled', 'disabled'));

        event.target.setAttribute('disabled', 'disabled');

        const list = Object
            .keys(uniqueProducts)
            .join(', ');

        textAreaElement.textContent += `You bought ${list} for ${totalPrice.toFixed(2)}.`
    })
}