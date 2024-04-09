function attachEvents() {
    let locationsUrl = 'http://localhost:3030/jsonstore/forecaster/locations'
    let currentUrl = 'http://localhost:3030/jsonstore/forecaster/today/'
    let upcomingUrl = 'http://localhost:3030/jsonstore/forecaster/upcoming/'
    let wantedLocationElement = document.getElementById('location')
    let submitButtonElement = document.getElementById('submit')
    submitButtonElement.addEventListener('click', getWeatherEvent)

    let forecastElement = document.getElementById('forecast')
    let currentConditionsElement = document.getElementById('current')
    let upcomingConditionsElement = document.getElementById('upcoming')

    let weatherSymbols = {
        'Sunny': '&#x2600',         // ☀
        'Partly sunny': '&#x26C5',  // ⛅
        'Overcast': '&#x2601',      // ☁
        'Rain': '&#x2614',          // ☂
        'Degrees': '&#176'          // °
    }


    function getWeatherEvent() {
        fetch(locationsUrl)
        .then(response => response.json())
        .then(data => {
            forecastElement.style.display = 'block'

            for (let location of data) {
                if (location.name === wantedLocationElement.value) {
                    let currentLocationCode = location.code

                    fetch(currentUrl + currentLocationCode)
                        .then(response => response.json())
                        .then(data => {
                            let divElement = document.createElement('div')
                            divElement.className = 'forecasts'
                            divElement.innerHTML = `
                            <span class="condition symbol">${weatherSymbols[data.forecast.condition]}</span>
                            <span class="condition">
                                <span class="forecast-data">${data.name}</span>
                                <span class="forecast-data">${data.forecast.low}${weatherSymbols['Degrees']}/${data.forecast.high}${weatherSymbols['Degrees']}</span>
                                <span class="forecast-data">${data.forecast.condition}</span>
                            </span>
                            `

                            currentConditionsElement.appendChild(divElement)
                        })

                    fetch(upcomingUrl + currentLocationCode)
                        .then(response => response.json())
                        .then(data => {
                            let divElement = document.createElement('div')
                            divElement.className = 'forecast-info'
                            for (let dayForecast of data.forecast) {
                                let newSpan = document.createElement('span')
                                newSpan.className = 'upcoming'
                                newSpan.innerHTML = `
                                <span class="symbol">${weatherSymbols[dayForecast.condition]}</span>
                                <span class="forecast-data">${dayForecast.low}${weatherSymbols['Degrees']}/${dayForecast.high}${weatherSymbols['Degrees']}</span>
                                <span class="forecast-data">${dayForecast.condition}</span>
                                `
                                divElement.appendChild(newSpan)
                            }

                            upcomingConditionsElement.appendChild(divElement)
                        })
                }
            }
        })
        .catch(() => {
            const divElement = document.createElement('div')
            divElement.textContent = 'Error';

            forecastElement.appendChild(divElement).style.display = 'block'
        })
    }
}

attachEvents();