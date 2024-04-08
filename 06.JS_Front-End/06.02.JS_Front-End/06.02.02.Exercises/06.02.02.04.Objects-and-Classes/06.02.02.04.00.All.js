// 01. Employees;
function solveEmployees(inputEmployees) {
    let employeesObject = {}

    inputEmployees.forEach(line => {
        const [employeeName, personalNumber] = [line, line.length];

        employeesObject[employeeName] = personalNumber;
    })

    for (const employee in employeesObject) {
        console.log(`Name: ${employee} -- Personal Number: ${employeesObject[employee]}`);
    }
}

solveEmployees(
    [
        'Silas Butler',
        'Adnaan Buckley',
        'Juan Peterson',
        'Brendan Villarreal'
    ]
);
solveEmployees(
    [
        'Samuel Jackson',
        'Will Smith',
        'Bruce Willis',
        'Tom Holland'
    ]
);


// 02. Towns;
function solveTowns(inputTowns) {
    let townsObject = {};

    inputTowns.forEach(line => {
        const [townName, latitudeValue, longitudeValue] = line.split(' | ');

        // Convert latitude and longitude values to numbers and round them to two decimal places
        const latitude = Number(latitudeValue).toFixed(2);
        const longitude = Number(longitudeValue).toFixed(2);

        townsObject = {
            town: townName,
            latitude: latitude.toString(),
            longitude: longitude.toString()
        };

        console.log(townsObject);
    })
}

solveTowns(
    [
        'Sofia | 42.696552 | 23.32601',
        'Beijing | 39.913818 | 116.363625'
    ]
);
solveTowns(
    [
        'Plovdiv | 136.45 | 812.575'
    ]
);


// 03. Store Provision;
function solveStoreProvisions(currentStock, orderedProducts) {
    let storeObject = {}

    for (let i = 0; i < currentStock.length; i += 2) {
        storeObject[currentStock[i]] = Number(currentStock[i + 1]);
    }

    for (let i = 0; i < orderedProducts.length; i += 2) {
        if (!storeObject[orderedProducts[i]]) {
            storeObject[orderedProducts[i]] = 0;
        }

        storeObject[orderedProducts[i]] += Number(orderedProducts[i + 1]);
    }

    for (const product in storeObject) {
        console.log(`${product} -> ${storeObject[product]}`);
    }
}

solveStoreProvisions(
    [
        'Chips', '5', 'CocaCola', '9', 'Bananas', '14', 'Pasta', '4', 'Beer', '2'
    ],
    [
        'Flour', '44', 'Oil', '12', 'Pasta', '7', 'Tomatoes', '70', 'Bananas', '30'
    ]
);
solveStoreProvisions(
    [
        'Salt', '2', 'Fanta', '4', 'Apple', '14', 'Water', '4', 'Juice', '5'
    ],
    [
        'Sugar', '44', 'Oil', '12', 'Apple', '7', 'Tomatoes', '7', 'Bananas', '30'
    ]
);


// 04. Movies;
function solveMovies(inputCommands) {
    let moviesArray = [];

    const addMovieCommand = 'addMovie';
    const directedByCommand = 'directedBy';
    const onDateCommand = 'onDate';

    for (const currentRow of inputCommands) {
        if (currentRow.includes(addMovieCommand)) {
            const movie = {
                name: currentRow.substring(addMovieCommand.length + 1)
            }

            moviesArray.push(movie)
        } else if (currentRow.includes(directedByCommand)) {
            const [movieName, movieDirector] = currentRow.split(` ${directedByCommand} `);
            const movie = moviesArray.find(movieToFind => movieToFind.name === movieName);

            if (movie) {
                movie.director = movieDirector;
            }
        } else if (currentRow.includes(onDateCommand)) {
            const [movieName, movieDate] = currentRow.split(` ${onDateCommand} `);
            const movie = moviesArray.find(movieToFind => movieToFind.name === movieName);

            if (movie) {
                movie.date = movieDate;
            }
        }
    }

    moviesArray
        .filter(movie => movie.director && movie.date)
        .forEach(movie => console.log(JSON.stringify(movie)))
}

solveMovies(
    [
        'addMovie Fast and Furious',
        'addMovie Godfather',
        'Inception directedBy Christopher Nolan',
        'Godfather directedBy Francis Ford Coppola',
        'Godfather onDate 29.07.2018',
        'Fast and Furious onDate 30.07.2018',
        'Batman onDate 01.08.2018',
        'Fast and Furious directedBy Rob Cohen'
    ]
);
solveMovies(
    [
        'addMovie The Avengers',
        'addMovie Superman',
        'The Avengers directedBy Anthony Russo',
        'The Avengers onDate 30.07.2010',
        'Captain America onDate 30.07.2010',
        'Captain America directedBy Joe Russo'
    ]
);


// 05. Inventory;
function solveInventory(inputHeroes) {
    let heroesCompendium = [];

    for (const currentHero of inputHeroes) {
        const [heroName, heroLevel, ...heroItems] = currentHero.split(' / ');

        const heroData = {
            name: heroName,
            level: Number(heroLevel),
            items: heroItems.join(', '),
        }

        heroesCompendium.push(heroData)
    }

    heroesCompendium
        .sort((a, b) => a.level - b.level)
        .forEach(hero => {
        console.log(`Hero: ${hero.name}`);
        console.log(`level => ${hero.level}`);
        console.log(`items => ${hero.items}`);
        })
}

solveInventory(
    [
        'Isacc / 25 / Apple, GravityGun',
        'Derek / 12 / BarrelVest, DestructionSword',
        'Hes / 1 / Desolator, Sentinel, Antara'
    ]
);
solveInventory(
    [
        'Batman / 2 / Banana, Gun',
        'Superman / 18 / Sword',
        'Poppy / 28 / Sentinel, Antara'
    ]
);


// 06. Words Tracker;
function solveWordsTracker(inputArray) {
    let wordCounter = {}

    const words = inputArray[0].split(' ');
    const wordsToSearch = inputArray.splice(1);

    for (const word of words) {
        wordCounter[word] = 0;

        for (const currentWord of wordsToSearch) {
            if (currentWord === word) {
                wordCounter[word] += 1;
            }
        }
    }

    const wordCounterDescending  = Object
        .entries(wordCounter)
        .sort((a, b) => b[1] - a[1]);

    for (const [word, occurrences] of wordCounterDescending) {
        console.log(`${word} - ${occurrences}`)
    }
}

solveWordsTracker(
    [
        'this sentence',
        'In', 'this', 'sentence', 'you', 'have', 'to', 'count', 'the', 'occurrences', 'of', 'the', 'words', 'this', 'and', 'sentence', 'because', 'this', 'is', 'your', 'task'
    ]
);
solveWordsTracker(
    [
        'is the',
        'first', 'sentence', 'Here', 'is', 'another', 'the', 'And', 'finally', 'the', 'the', 'sentence'
    ]
);

// 07. Odd Occurrences;
function solveOddOccurrences(inputString) {
    let wordOccurrences = {};
    const words = inputString.split(' ').map(word => word.toLowerCase())

    for (const word of words) {
        if (!wordOccurrences.hasOwnProperty(word)) {
            wordOccurrences[word] = 0;
        }
        wordOccurrences[word] += 1;
    }

    let oddWordOccurrences = [];

    for (const word in wordOccurrences) {
        if (wordOccurrences[word] % 2 !== 0) {
            oddWordOccurrences.push(word)
        }
    }

    console.log(oddWordOccurrences.join(' '))
}

solveOddOccurrences('Java C# Php PHP Java PhP 3 C# 3 1 5 C#');
solveOddOccurrences('Cake IS SWEET is Soft CAKE sweet Food');


// 08. Piccolo;
function solvePiccolo(inputCars) {
    let parkingLot = [];

    for (const line of inputCars) {
        const [direction, licensePlate] = line.split(', ')

        if (direction === 'IN') {
            parkingLot.push(licensePlate);
        } else if (direction === 'OUT') {
            const carIndex = parkingLot.indexOf(licensePlate);

            if (carIndex !== -1) {
                parkingLot.splice(carIndex, 1);
            }
        }
    }

    parkingLot.sort((a, b) => a.localeCompare(b));

    if (parkingLot.length === 0) {
        console.log('Parking Lot is Empty');
    } else {
        for (const car of parkingLot) {
            console.log(car);
        }
    }
}

solvePiccolo(
    [
        'IN, CA2844AA',
        'IN, CA1234TA',
        'OUT, CA2844AA',
        'IN, CA9999TT',
        'IN, CA2866HI',
        'OUT, CA1234TA',
        'IN, CA2844AA',
        'OUT, CA2866HI',
        'IN, CA9876HH',
        'IN, CA2822UU'
    ]
);
solvePiccolo(
    [
        'IN, CA2844AA',
        'IN, CA1234TA',
        'OUT, CA2844AA',
        'OUT, CA1234TA'
    ]
);


// 09. Make a Dictionary;


// 10. Class Vehicle;


