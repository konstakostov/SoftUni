function solve() {
    document.querySelector('#btnSend').addEventListener('click', onClick);

    function onClick() {
        const inputText = document.querySelector('div#inputs textarea').value;
        const bestRestaurantElement = document.querySelector('div#bestRestaurant p');
        const bestWorkersElement = document.querySelector('div#workers p');

        let dataList = inputText.replace(/[\[\]"]/g, '').trim().split(',');

        let restaurants = {};

        let restaurantName = '';

        for (let i = 0; i < dataList.length; i++) {
            if (dataList[i].includes('-')) {
                restaurantName = dataList[i]
                    .slice(0, dataList[i]
                        .indexOf('-'))
                    .trim();
                const [person, salary] = dataList[i]
                    .slice(dataList[i]
                        .indexOf('-') + 1)
                    .trim()
                    .split(' ');

                if (restaurants.hasOwnProperty(restaurantName)) {
                    restaurants[restaurantName].push(person);
                    restaurants[restaurantName].push(Number(salary));
                } else {
                    const [person, salary] = dataList[i]
                        .slice(dataList[i]
                            .indexOf('-') + 1)
                        .trim()
                        .split(' ');
                    restaurants[restaurantName] = [person, Number(salary)];
                }
            } else {
                const [person, salary] = dataList[i]
                    .slice(dataList[i]
                        .indexOf('-') + 1)
                    .trim()
                    .split(' ');

                restaurants[restaurantName].push(person);
                restaurants[restaurantName].push(Number(salary));
            }

            if (i + 1 < dataList.length && dataList[i + 1].includes('-')) {
                restaurantName = '';
            }
        }

        let highestAverageSalary = 0;
        let highestSalary = 0;
        let bestRestaurantName = '';
        let bestEmployees = [];

        Object
            .keys(restaurants)
            .forEach(restaurant => {
                const employees = restaurants[restaurant];
                let currentSalarySum = 0;
                let currentHighestSalary = 0;

                let currentBestEmployees = {};

                for (let i = 0; i < employees.length; i += 2) {
                    const name = employees[i];
                    const salary = Number(employees[i + 1]);

                    currentSalarySum += salary;

                    if (currentHighestSalary < salary) {
                        currentHighestSalary = salary;
                    }

                    currentBestEmployees[name] = salary;
                }

                const currentSalaryAverage = currentSalarySum / Object.keys(currentBestEmployees).length;

                // Changed to convert the object into an array of key-value pairs
                const currentBestEmployeesSorted = Object.entries(currentBestEmployees)
                    .sort((a, b) => b[1] - a[1]);

                // Changed to sort the array of key-value pairs, not the object directly
                const sortedEmployeesObject = Object.fromEntries(currentBestEmployeesSorted);


                let employeesData = []

                Object
                    .keys(sortedEmployeesObject)
                    .forEach(person =>
                        employeesData.push(`Name: ${person} With Salary: ${sortedEmployeesObject[person]}`))

                if (currentSalaryAverage > highestAverageSalary) {
                    highestAverageSalary = currentSalaryAverage;
                    highestSalary = currentHighestSalary;
                    bestEmployees = employeesData;
                    bestRestaurantName = restaurant.toString();
                }
            })

        bestRestaurantElement.textContent = `Name: ${bestRestaurantName} Average Salary: ${highestAverageSalary.toFixed(2)} Best Salary: ${highestSalary.toFixed(2)}`
        bestWorkersElement.textContent = bestEmployees.join(' ');
    }
}