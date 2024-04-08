function attachEventsListeners() {
    const convertButtonElements = document.querySelectorAll('input[value=Convert]');
    const inputElements = document.querySelectorAll('input[type=text]')

    function toSeconds(value, unit) {
        switch (unit) {
            case 'days':
                return  value * 60 * 60 * 24;
            case 'hours':
                return  value * 60 * 60;
            case 'minutes':
                return  value * 60;
            case 'seconds':
                return  value;
        }
    }

    const convertors = {
        days(seconds) {
            return seconds / 60 / 60 / 24;
        },
        hours(seconds) {
            return seconds / 60 / 60;
        },
        minutes(seconds) {
            return seconds / 60;
        },
        seconds(seconds) {
            return seconds;
        }
    }

    for (const convertButton of convertButtonElements) {
        convertButton.addEventListener('click', (e) => {
            const currentInputElement = e.currentTarget.parentElement.querySelector('input[type=text]');

            for (const inputElement of inputElements) {
                const seconds = toSeconds(Number(currentInputElement.value), currentInputElement.id);
                inputElement.value = convertors[inputElement.id](seconds);
            }
        })
    }
}