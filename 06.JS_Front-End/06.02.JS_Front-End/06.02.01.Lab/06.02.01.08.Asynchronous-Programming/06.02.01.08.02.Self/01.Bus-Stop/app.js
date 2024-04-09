function getInfo() {
    const baseUrl = 'http://localhost:3030/jsonstore/bus/businfo/';

    const inputStopElement = document.getElementById('stopId');
    const checkButtonElement = document.getElementById('submit');

    const stopNameElement = document.getElementById('stopName');
    const busListElement = document.getElementById('buses');

    const stopId = inputStopElement.value;

    busListElement.innerHTML = '';

    fetch(`${baseUrl}${stopId}`)
        .then(response => response.json())
        .then(data => {
            stopNameElement.textContent = data.name;

            for (const busId in data.buses) {
                const liElement = document.createElement('li');
                liElement.textContent = `Bus ${busId} arrives in ${busId.time} minutes`;

                busListElement.appendChild(liElement);
            }
        })
        .catch(() => {
            stopNameElement.textContent = 'Error';
        })
}