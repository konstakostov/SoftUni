function solve() {
    const baseUrl = 'http://localhost:3030/jsonstore/bus/schedule/'

    const infoBoxElement = document.getElementById('info');
    const departButtonElement = document.getElementById('depart');
    const arriveButtonElement = document.getElementById('arrive');

    arriveButtonElement.disabled = 'disabled';

    let nameNextStop = '';
    let idNextStop = 'depot';


    function depart() {
        fetch(baseUrl + idNextStop)
            .then(response => response.json())
            .then(data => {
                infoBoxElement.textContent = `Next stop ${data.name}`;

                nameNextStop = data.name;
                idNextStop = data.next;

                departButtonElement.disabled = true;
                arriveButtonElement.disabled = false;
            })
            .catch(() => {
                    infoBoxElement.textContent = "Error"
                    departButtonElement.disabled = true
                    arriveButtonElement.disabled = true
                })
    }

    async function arrive() {
        infoBoxElement.textContent = `Arriving at ${nameNextStop}`;

        departButtonElement.disabled = false;
        arriveButtonElement.disabled = true;
    }

    return {
        depart,
        arrive
    };
}

let result = solve();