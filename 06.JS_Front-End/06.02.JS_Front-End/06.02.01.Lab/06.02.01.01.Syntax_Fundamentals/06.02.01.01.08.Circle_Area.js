function circleArea01(num) {
    let result;

    if (typeof num === "number") {
        result = (Math.PI * (num ** 2)).toFixed(2);
    } else {
        result = 'We can not calculate the circle area, because we receive a {type of argument}.'
    }

    console.log(result);
}

circleArea01(5)
circleArea01('name')

function circleArea02(num) {
    let result;
    let inputType = typeof(num);

    if (inputType === 'number') {
        result = Math.pow(num, 2) * Math.PI;
        result = result.toFixed(2);
    } else {
        result = 'We can not calculate the circle area, because we receive a {type of argument}.'
    }

    console.log(result);
}

circleArea02(5)
circleArea02('name')
