/*
Asynchronous Programming

- Structured using callback function;
- In current JS:
    - Callbacks;
    - Promises;
    - Async Functions;

- It is different from concurrent or multi-thread programming;

- JS code is generally single-threaded;

- Asynchronous programming allows running several tasks (pieces of code) in parallel, at the same time;
- Synchronous programming does not allow running several tasks (pieces of code) in parallel, instead it runs them on by one;

- Callback;
    - Function passed into another function as an argument then invoked inside the outer function to complete some kind
    of routine or action;
*/

// Async programming with Callback;
console.log('Start');
delayStart(() => console.log('Delayed Start'));
console.log('Finish');

function delayStart(callback) {
    setTimeout(() => {
        callback();
    }, 100);
}


/*
Promises Basics;
- Promise -> Asynchronous action that may complete at some point and produce a value;

- Promise States;
    - Pending -> Operation still running (unfinished);
    - Fulfilled -> Operation finished (the result is available);
    - Failed -> Operation failed (an error is present);

- Promises use the Promise class;
    - new Promise(executor);


*/
// Promise
const weddingPromise = new Promise((resolve, reject) => {
    if (Math.random() < 0.3) {
        return reject('I am Sorry, it\'s me!');
    }

    setTimeout(() => {
        resolve('Just Married!')
    }, 1000)
})

weddingPromise
    .then((message) => {
        console.log(message);
    })
    .catch(message => {
        console.log(message);
    })
    .finally(() => {
        console.log('Love always wins!')
    });

// Always rejecting Promise;
const rejectPromise = Promise.reject('Sorry, next time.')
console.log(rejectPromise)
rejectPromise.catch((message) => console.log(message));

// Multiple parallel promises;
const createTimeoutPromise = function(message, time) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve(message)
        }, time);
    });
}

const groupPromise = Promise.all([
    Promise.resolve('First Promise'),
    createTimeoutPromise('Second Promise', 2000),
    createTimeoutPromise('Third Promise', 3000),
])

groupPromise
    .then((values) => {
        console.log(values)
    })
    .catch(error => {
        console.log(error)
    });


/*
AJAX & Fetch API
- Asynchronous JavaScript and XML (AJAX);

- Background loading of dynamic content/data;
- Loads data from web server and renders it;

- Examples of AJAX usage;
    - Partial page rendering (Loads HTML fragment + shows it in a <div>);
    - Loads JSON object and displays it;

- Fetch API;
    - Allows making network requests;
    - Uses Promises;
    - Enables simpler and cleaner API;
    - Makes code more readable & maintainable;


- Basic Fetch Request;
    - Response is a Stream object;
    - The Stream is read asynchronously;
    - When json() method is called, a Promise is returned;

*/



/*
ES6 Async/Await


*/


