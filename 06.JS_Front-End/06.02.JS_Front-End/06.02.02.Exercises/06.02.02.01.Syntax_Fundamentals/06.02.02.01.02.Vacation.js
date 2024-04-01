function solve(groupSize, groupType, day) {
    let singlePrice;
    let totalPrice;

    if (day === 'Friday') {
        if (groupType === 'Students') {
            singlePrice = 8.45;
        } else if (groupType === 'Business') {
            singlePrice = 10.90;
        } else if (groupType === 'Regular') {
            singlePrice = 15;
        }
    } else if (day === 'Saturday') {
        if (groupType === 'Students') {
            singlePrice = 9.80;
        } else if (groupType === 'Business') {
            singlePrice = 15.60;
        } else if (groupType === 'Regular') {
            singlePrice = 20;
        }
    } else if (day === 'Sunday') {
        if (groupType === 'Students') {
            singlePrice = 10.46;
        } else if (groupType === 'Business') {
            singlePrice = 16;
        } else if (groupType === 'Regular') {
            singlePrice = 22.50;
        }
    }

    totalPrice = groupSize * singlePrice;

    if (groupType === 'Students' && groupSize >= 30) {
        totalPrice *= (1 - 0.15);
    } else if (groupType === 'Business' && groupSize >= 100) {
        totalPrice -= (10 * singlePrice);
    } else if (groupType === 'Regular' && (groupSize >= 10 && groupSize <= 20)) {
        totalPrice *= (1 - 0.05);
    }

    console.log(`Total price: ${totalPrice.toFixed(2)}`)
}

solve(
    30,
    "Students",
    "Sunday"
);
solve(
    40,
    "Regular",
    "Saturday"
);
