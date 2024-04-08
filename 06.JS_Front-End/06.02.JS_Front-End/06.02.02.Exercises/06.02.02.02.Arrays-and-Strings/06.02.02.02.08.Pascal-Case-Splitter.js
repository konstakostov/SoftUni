function solve(inputString) {
    const pattern = /[A-Z][a-z]*/g;
    const finalArray = inputString.match(pattern);

    console.log(finalArray.join(', '));
}

solve('SplitMeIfYouCanHaHaYouCantOrYouCan')
solve('HoldTheDoor')
solve('ThisIsSoAnnoyingToDo')