function solve(inputArray) {
    class Song {
        constructor(type, name, time) {
            this.type = type;
            this.name = name;
            this.time = time;
        }
    }

    let songs = [];
    let numberOfSongs = inputArray.shift()
    const songType = inputArray.pop()

    for (let i = 0; i < numberOfSongs; i++) {
        let [songType, songName, songTime] = inputArray[i].split('_');
        songs.push(new Song(songType, songName, songTime));
    }

    if (songType === 'all') {
        songs.forEach(song => console.log(song.name))
    } else {
        songs
            .filter(song => song.type === songType)
            .forEach(song => console.log(song.name));
    }
}

solve(
    [3,
        'favourite_DownTown_3:14',
        'favourite_Kiss_4:16',
        'favourite_Smooth Criminal_4:01',
        'favourite']
);
solve(
    [
        4,
        'favourite_DownTown_3:14',
        'listenLater_Andalouse_3:24',
        'favourite_In To The Night_3:58',
        'favourite_Live It Up_3:48',
        'listenLater'
    ]
);
solve(
    [
        2,
        'like_Replay_3:15',
        'ban_Photoshop_3:48',
        'all'
    ]
);