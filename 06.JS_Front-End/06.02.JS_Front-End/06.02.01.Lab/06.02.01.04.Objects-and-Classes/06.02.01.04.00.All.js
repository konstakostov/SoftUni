/*
Objects;
- The Object is a structure of related data or functionality;
- Objects contains values, that can be accessed by string keys; The data values are called properties; Values can be
different types; Functions are called methods;
- Properties can e added and removed during runtime;
- Dot syntax recognises only standard identifiers;
- Bracket syntax  is used to recognise standard & non-standard identifiers;
*/

// Creating an empty object;
let emptyObject = {};

console.log(emptyObject);


// Creating an object;
let person01 = {name: 'George', age: '20'};

console.log(person01);

// Creating an object with non-class identifiers
let person02 = {'full-name': 'John Smith', age: 30};

console.log(person02);

// Using dot syntax to get property value;
console.log(person01.name);

// Using bracket syntax to get property value;
console.log(person02['full-name']);
console.log(person02['age']);


// Dynamically add values to object with dot syntax;
const animal = {};
animal.name = 'Peter';

console.log(animal)

// Dynamically add values to object with bracket syntax;
animal['min-weight'] = 2;

console.log(animal)

// Adding dynamic name property;
const propName = 'type';
animal[propName] = 'Cat'

console.log(animal)

// Adding dynamic name property in the literal;
const dynamicPropName = 'fullName';
const person03 = {
    [dynamicPropName]: 'Jane Doe'
}

console.log(person03)

// Object literal with shorthand syntax;
function solveShortPersonInfo(firstName, lastName, age) {
    const shortPersonInfo = {
        firstName,
        lastName,
        age,
    }

    return shortPersonInfo;
}

// shortPersonInfo is equivalent to longPersonInfo;

function solvelongPersonInfo(firstName, lastName, age) {
    const longPersonInfo = {
        firstName: firstName,
        lastName: lastName,
        age: age,
    }

    return longPersonInfo;
}


/*
Object methods;
- Defining method in object literal with function expression or arrow function;

- Object.keys(): Get an array  of all property names (keys);
- Object.values(): Get an array  of all property values;
- Object.entries() Gen an array of all properties as key-value tuples;;
*/

// Define method in object literal;
const cat = {
    name: 'Ben',
    breed: 'Persian',
    age: '12',
    grades: [5, 6, 5, 6 ,6 ,6],
    owner: {
        name: 'John',
        age: 32,
    },
    // Function expression value;
    makeSound: function () {
        console.log('Meow');
    },
    // Arrow function;
    sleep: () => console.log('Zzz')
}

// Call method from object;
cat.makeSound();    // Most used way
cat['makeSound']();
let methodName = 'makeSound';
cat[methodName]();

// Adding method dynamically;
cat.eat = function() {
    console.log('Om nom nom nom...');
}

cat.eat();

// Using method notation syntax;
const dog = {
    name: 'Lucky',
    breed: 'Not Available',
    makeSound() {
        console.log('Woof');
    },
    ownerName: 'Janice',
}


// Get all property names of an object;
const propertyNames = Object.keys(cat);

console.log(propertyNames);

// Get all property values of an object;
const propertyValues = Object.values(cat);

console.log(propertyValues);

// Get object key value pairs;
const propertyKeyValuePairs = Object.entries(cat);

console.log(propertyKeyValuePairs);


/*
JSON;
- Stands for JavaScript Object Notation;
- Open-standard file format, using text-to-transmit data objects;
- Language independent. 'self-describing' and easy to understand;
- It is used to exchange data between browser and server;
- Lightweight (compared to XML);
- JS has built-in function to parse JSON;

JSON Example;
{
    "name": "John",
    "age": "25",
    "grades": {
        "Math": [2.50, 3.50],
        "Chemistry": [4.50],
    },
}

Some of JSON characteristics;
- The {} define a JSON;
- Keys are in "" always;
- Keys and Values are separated by ':';
- Nested objects are allowed;
- Arrays, Objects, Numbers, Strings, Bool can be used;

*/

// Convert JS object to JSON;
const dogToJSON = JSON.stringify(dog);  // This is a string;

console.log(dogToJSON);

// Convert JSON to JS object;
const dogJSONtoDogJS = JSON.parse(dogToJSON);   // This is an object;

console.log(dogJSONtoDogJS);


/*
Associative Arrays;
- They are objects; They can be declared dynamically, too.
- Arrays, indexed by string keys;
- Holds a set of pairs [key => value], where the key is a string and the value can be any type;

Sorting
*/

// Creating associative array;
let fullName01 = 'Janice Joplin';
let fullName02 = 'Jenny Hills';

let phoneBook = {
    'Jane Doe': '+359888111111',
    'John Smith': '+359888222222',
    [fullName01]: '359888333333',
};

phoneBook['James Black'] = '+359888444444';
phoneBook[fullName02] = '+359888555555';

console.log(phoneBook);

// For-in Loop for associative array;
for (let name in phoneBook) {
    console.log(`${name}: ${phoneBook[name]}`);  // Keys: Values;
}

// For-in Loop in array; DO NOT USE FOR REGULAR ARRAYS!!! It iterates through the indices!!!
const namesArray01 = ['Jane', 'Janice', 'Jenny'];
for (const name in namesArray01) {
    console.log(name);
}

// Checking if key is in associative array and remove it;
if (phoneBook.hasOwnProperty("Jenny Hills")) {
    delete phoneBook['Jenny Hills']
}

console.log(phoneBook);

// Sorting an Object;
let sortedPhonebook = Object
    .entries(phoneBook)
    .sort((a, b) => a[0].localeCompare(b[0]));

console.log(sortedPhonebook);

// Turn Sorted Object back into array
phoneBook = Object.fromEntries(sortedPhonebook);

console.log(phoneBook)

// Object destructuring assignment;
const personData01 = {
    name: "Janice",
    age: 24,
    height: '156cm',
};

const {age: personAge, name: personName} = personData01;

console.log(personName, personAge);

// Object destructuring assignment with rest;
const {name: personalName, ...restPersonInfo} = personData01;

console.log(personalName, restPersonInfo);


/*
Classes;
- Templates for creating objects;
- They define structure & behaviour;
- Object, created by class patters is called Instance of that class;
- The class has constructor - method, called automatically to create an abject, prepare the object to be used; The
constructor can receive parameters and assign properties to them;

- 'this; keyword is used to set a property of the object to a given value;
*/

// Creating a class;
class Person {
    constructor(firstName, lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }

    // Creating a method;
    greet() {
        console.log(`Hello to ${this.firstName}!`);
    }
}

// Creating an object from the class;
const newPerson01 = new Person('John', 'Smith');
const newPerson02 = new Person('Jane', 'Doe');

console.log(newPerson01);
console.log(newPerson02);

// Calling the method;
newPerson01.greet()
newPerson02.greet()

// 01. Person Info;
function solvePersonalInfo(firstName, lastName, age) {
    const personalInfo = {
        firstName,
        lastName,
        age,
    };

    return personalInfo;
}

console.log(solvePersonalInfo("Peter", "Pan","20"));
console.log(solvePersonalInfo("George", "Smith","18"));

// 02. City;
function solveCity(cityObject) {
    Object
        .keys(cityObject)
        .forEach(propertyName => console.log(`${propertyName} -> ${cityObject[propertyName]}`))
}

solveCity(
    {
        name: "Sofia",
        area: 492,
        population: 1238438,
        country: "Bulgaria",
        postCode: "1000"
    }
);
solveCity(
    {
        name: "Plovdiv",
        area: 389,
        population: 1162358,
        country: "Bulgaria",
        postCode: "4000"
    }
);


// 03. Convert to Object;
function solveConvertToObject(input) {
    const personData = JSON.parse(input);

    Object
        .keys(personData)
        .forEach(key => console.log(`${key}: ${personData[key]}`))
}

solveConvertToObject('{"name": "George", "age": 40, "town": "Sofia"}');
solveConvertToObject('{"name": "Peter", "age": 35, "town": "Plovdiv"}');


// 04. Convert to JSON;
function solveConvertToJSON(firstName, lastName, hairColor) {
    const personInfo = {
        name: firstName,
        lastName,
        hairColor,
    };

    const personInfoJSON = JSON.stringify(personInfo);

    console.log(personInfoJSON)
}

solveConvertToJSON('George', 'Jones', 'Brown');
solveConvertToJSON('Peter', 'Smith', 'Blond');


// 05. Phone Book;
function solvePhoneBook(inputRecords) {
    const phoneBook = {};

    for (const line of inputRecords) {
        const [name, phone] = line.split(' ');
        phoneBook[name] = phone;
    }

    for (const name in phoneBook) {
        console.log(`${name} -> ${phoneBook[name]}`)
    }
}

solvePhoneBook(
    [
        'Tim 0834212554',
        'Peter 0877547887',
        'Bill 0896543112',
        'Tim 0876566344'
    ]
);

solvePhoneBook(
    [
        'George 0552554',
        'Peter 087587',
        'George 0453112',
        'Bill 0845344'
    ]
);


// 06. Meetings;
function solveMeetings(inputMeetings) {
    const meetings = {};

    for (const line of inputMeetings) {
        const [weekday, name] = line.split(' ');

        if (meetings[weekday]) {
            console.log(`Conflict on ${weekday}!`);
        } else {
            meetings[weekday] = name;
            console.log(`Scheduled for ${weekday}`);
        }
    }

    for (const day in meetings) {
        console.log(`${day} -> ${meetings[day]}`)
    }
}

solveMeetings(
    [
        'Monday Peter',
        'Wednesday Bill',
        'Monday Tim',
        'Friday Tim'
    ]
);

solveMeetings(
    [
        'Friday Bob',
        'Saturday Ted',
        'Monday Bill',
        'Monday John',
        'Wednesday George'
    ]
);


// 07. Address Book;
function solveAddressBook(inputAddresses) {
    // First solution;
    const addressBook = {};

    inputAddresses.forEach(line => {
        const [name, address] = line.split(':');

        addressBook[name] = address;
    });

    Object
        .entries(addressBook)
        .sort((a, b) => a[0].localeCompare(b[0]))
        .forEach(([name, address]) => console.log(`${name} -> ${address}`));
}

// function solveAddressBook(inputAddresses) {
//     // Second solution;
//     const addressBook = inputAddresses.reduce((book, line) => {
//             const [name, address] = line.split(':');
//
//             book[name] = address;
//
//             return book;
//         }
//     )
// }

solveAddressBook(
    [
        'Tim:Doe Crossing',
        'Bill:Nelson Place',
        'Peter:Carlyle Ave',
        'Bill:Ornery Rd'
    ]
)

solveAddressBook(
    [
        'Bob:Huxley Rd',
        'John:Milwaukee Crossing',
        'Peter:Fordem Ave',
        'Bob:Redwing Ave',
        'George:Mesta Crossing',
        'Ted:Gateway Way',
        'Bill:Gateway Way',
        'John:Grover Rd',
        'Peter:Huxley Rd',
        'Jeff:Gateway Way',
        'Jeff:Huxley Rd'
    ]
)


// 08. Cats;


function solveCats(inputCats) {
    class Cat {
        constructor(name, age) {
            this.name = name;
            this.age = Number(age);
        }

        meow() {
            console.log(`${this.name}, age ${this.age} says Meow`)
        }
    }

    inputCats
        .map(line => line.split(' '))
        .map(([name, age]) => new Cat(name, age))
        .forEach(cat => cat.meow());
}

solveCats(['Mellow 2', 'Tom 5']);
solveCats(['Candy 1', 'Poppy 3', 'Nyx 2']);


// 09. Songs;
function solveSongs(inputSongs) {
    class Song {
        constructor(songName, songTime) {
            this.songName = songName;
            this.songTime = songTime;
        }
    }

    const songCollection = {};
    const allSongs = [];

    const numberOfSongs = inputSongs.shift();

    for (let i = 0; i < numberOfSongs; i++) {
        const [typeList, name, time] = inputSongs.shift().split('_');

        if (!songCollection[typeList]) {
            songCollection[typeList] = [];
        }

        const currentSong = new Song(name, time);
        songCollection[typeList].push(currentSong);
        allSongs.push(currentSong);
    }

    const songTypeList = inputSongs.shift();
    if (songTypeList === 'all') {
        allSongs.forEach(song => console.log(song.songName));
    } else {
        if (songCollection[songTypeList]) {
            songCollection[songTypeList].forEach(song => console.log(song.songName));
        } else {
            console.log("No songs found for the specified type.");
        }
    }
}


solveSongs(
    [
        3,
        'favourite_DownTown_3:14',
        'favourite_Kiss_4:16',
        'favourite_Smooth Criminal_4:01',
        'favourite'
    ]
);

solveSongs(
    [
        4,
        'favourite_DownTown_3:14',
        'listenLater_Andalouse_3:24',
        'favourite_In To The Night_3:58',
        'favourite_Live It Up_3:48',
        'listenLater'
    ]
);

solveSongs(
    [
        2,
        'like_Replay_3:15',
        'ban_Photoshop_3:48',
        'all'
    ]
);
