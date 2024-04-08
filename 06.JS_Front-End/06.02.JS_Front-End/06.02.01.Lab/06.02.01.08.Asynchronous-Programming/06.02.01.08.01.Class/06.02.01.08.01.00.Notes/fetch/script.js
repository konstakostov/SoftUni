const url = 'https://swapi.dev/api';

// Promise Chaining;
fetch(`${url}/people/1`)
    .then((response) => {
        return response.json();
    })
    .then(data => {
        console.log(data);
    })
    .catch(() => {
        console.log('An error occurred;');
    })


// Create book;
const urlBooks = 'http://localhost:3030/jsonstore/books';
fetch(urlBooks, {
    method: 'POST',
    headers: {
        'content-type': 'application/json'
    },
    body: JSON.stringify({
        title: "Lord of the Rings",
        author: 'J. R. R. Tolkien',
    })
})
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.log(error));


// Using local server to get blog;
fetch(urlBooks)
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.log(error));

// Create book;
