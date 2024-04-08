function solve(dayType, age) {
    if (age >= 0 && age <= 18) {
        if (dayType === 'Weekday') {
            console.log("12$")
        } else if (dayType === 'Weekend') {
            console.log("15$")
        } else if (dayType === 'Holiday') {
            console.log("5$")
        }
    } else if (age > 18 && age <= 64) {
        if (dayType === 'Weekday') {
            console.log("18$")
        } else if (dayType === 'Weekend') {
            console.log("20$")
        } else if (dayType === 'Holiday') {
            console.log("12$")
        }
    } else if (age > 64 && age <= 122) {
        if (dayType === 'Weekday') {
            console.log("12$")
        } else if (dayType === 'Weekend') {
            console.log("15$")
        } else if (dayType === 'Holiday') {
            console.log("10$")
        }
    } else {
        console.log('Error!')
    }
}

solve('Weekday', 42);
solve('Holiday', -12);
solve('Holiday', 15);