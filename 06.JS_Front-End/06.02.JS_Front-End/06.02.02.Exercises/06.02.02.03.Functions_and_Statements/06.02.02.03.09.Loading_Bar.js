function solve(number) {
    const percent = number / 10;

    if (number < 100) {
        console.log(`${number}% [${'%'.repeat(percent)}${'.'.repeat(10 - percent)}]`);
        console.log('Still loading...');
    } else {
        console.log(`[${'%'.repeat(percent)}]`);
        console.log('100% Complete!');
    }
}

solve(30);
solve(50);
solve(100);