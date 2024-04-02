function solve(inputArray) {
    class Cat {
        constructor(name, age) {
            this.name = name;
            this.age = Number(age);
        }

        meow() {
            console.log(`${this.name}, age ${this.age} says Meow`)
        }
    }

    inputArray
        .map(line => line.split(' '))
        .map(([name, age]) => new Cat(name, age))
        .forEach(cat => cat.meow());
}

solve(['Mellow 2', 'Tom 5']);
solve(['Candy 1', 'Poppy 3', 'Nyx 2']);