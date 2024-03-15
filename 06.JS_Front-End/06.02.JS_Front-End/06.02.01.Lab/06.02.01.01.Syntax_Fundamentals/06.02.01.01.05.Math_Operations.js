function operations(num01, num02, operator) {
    let result;
    switch (operator) {
        case '+': result = num01 + num02; break;
        case '-': result = num01 - num02; break;
        case '*': result = num01 * num02; break;
        case '/': result = num01 / num02; break;
        case '%': result = num01 % num02; break;
        case '**': result = num01 ** num02; break;
    }

    console.log(result)
}

operations(5, 6, '+')
operations(5, 6, '-')
operations(7, 2, '/')
operations(7, 2, '*')
operations(7, 7, '%')
operations(7, 2, '**')
