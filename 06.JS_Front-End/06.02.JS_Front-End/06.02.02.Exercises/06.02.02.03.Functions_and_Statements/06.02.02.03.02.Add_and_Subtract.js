function solve(x, y, z) {
    console.log(subtract(sum(x, y), z));

    function sum(x1, y1) {
        return x1 + y1;
    }

    function subtract(xy, z1) {
        return xy - z1;
    }
}

solve(23, 6, 10);
solve(1, 17, 30);
solve(42, 58, 100);