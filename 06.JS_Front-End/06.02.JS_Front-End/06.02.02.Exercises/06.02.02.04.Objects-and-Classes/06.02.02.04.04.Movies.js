function solve(inputArray) {
    let movies = [];

    const addMovieCommand = 'addMovie';
    const directedByCommand = 'directedBy';
    const onDateCommand = 'onDate';

    for (const line of inputArray) {
        if (line.includes(addMovieCommand)) {
            const movie = {
                name: line.substring(addMovieCommand.length + 1)
            };

            movies.push(movie)
        } else if (line.includes(directedByCommand)) {
            const [name, director] = line.split(` ${directedByCommand} `);

            const movie = movies.find(searchedMovie => searchedMovie.name === name);

            if (movie) {
                movie.director = director;
            }
        } else if (line.includes(onDateCommand)) {
            const [name, date] = line.split(` ${onDateCommand} `);

            const movie = movies.find(searchedMovie => searchedMovie.name === name);

            if (movie) {
                movie.date = date;
            }
        }
    }

    movies
        .filter(movie => movie.director && movie.date)
        .forEach(movie => console.log(JSON.stringify(movie)))
}

solve(
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
solve(
    [
        'addMovie The Avengers',
        'addMovie Superman',
        'The Avengers directedBy Anthony Russo',
        'The Avengers onDate 30.07.2010',
        'Captain America onDate 30.07.2010',
        'Captain America directedBy Joe Russo'
    ]
);