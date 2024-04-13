function solve(dataInput) {
    const numCharacters = dataInput.splice(0, 1)[0];

    let characters = {};

    const maxHP = 100;
    const maxBullets = 6;

    for (const characterData of dataInput.splice(0, numCharacters)) {
        const [name, hp, bullets] = characterData.split(' ');

        characters[name] = {
            hp: Number(hp),
            bullets: Number(bullets),
        }
    }

    for (const line of dataInput) {
        if (line === 'Ride Off Into Sunset') {
            Object
                .keys(characters)
                .forEach(name => {
                    console.log(`${name}`);
                    console.log(`  HP: ${characters[name].hp}`);
                    console.log(`  Bullets: ${characters[name].bullets}`);
                })

            break;
        } else if (line.startsWith('FireShot')) {
            const [, name, target] = line.split(' - ');

            if (characters[name].bullets > 0) {
                characters[name].bullets -= 1;
                console.log(`${name} has successfully hit ${target} and now has ${characters[name].bullets} bullets!`);
            } else {
                console.log(`${name} doesn't have enough bullets to shoot at ${target}!`);
            }
        } else if (line.startsWith('TakeHit')) {
            const [, name, damage, attacker] = line.split(' - ');

            characters[name].hp -= damage;

            if (characters[name].hp > 0) {
                console.log(`${name} took a hit for ${damage} HP from ${attacker} and now has ${characters[name].hp} HP!`);
            } else {
                delete characters[name];
                console.log(`${name} was gunned down by ${attacker}!`)
            }
        } else if (line.startsWith('Reload')) {
            const [, name] = line.split(' - ');

            if (characters[name].bullets < maxBullets) {
                const reloadedBullets = maxBullets - characters[name].bullets;
                characters[name].bullets = maxBullets;

                console.log(`${name} reloaded ${reloadedBullets} bullets!`);
            } else {
                console.log(`${name}'s pistol is fully loaded!`)
            }
        } else if (line.startsWith('PatchUp')) {
            const [, name, amountString] = line.split(' - ');

            const amount = Number(amountString);

            if (characters[name].hp === maxHP) {
                console.log(`${name} is in full health!`);
            } else {
                let hpRestored = amount;

                characters[name].hp += amount;

                if (characters[name].hp > maxHP) {
                    hpRestored = amount - (characters[name].hp - maxHP);
                    characters[name].hp = maxHP;
                }

                console.log(`${name} patched up and recovered ${hpRestored} HP!`)
            }
        }
    }
}

// solve(([
//     "2",
//     "Gus 100 0",
//     "Walt 100 6",
//     "FireShot - Gus - Bandit",
//     "TakeHit - Gus - 100 - Bandit",
//     "Reload - Walt",
//     "Ride Off Into Sunset"
// ]));
// /*
// Gus doesn't have enough bullets to shoot at Bandit!
// Gus was gunned down by Bandit!
// Walt's pistol is fully loaded!
// Walt
//  HP: 100
//  Bullets: 6
// */
//
// console.log();

solve(([
    "2",
    "Jesse 100 4",
    "Walt 100 5",
    "FireShot - Jesse - Bandit",
    "TakeHit - Walt - 30 - Bandit",
    "PatchUp - Walt - 20",
    "Reload - Jesse",
    "Ride Off Into Sunset"
]));
/*
Jesse has successfully hit Bandit and now has 3 bullets!
Walt took a hit for 30 HP from Bandit and now has 70 HP!
Walt patched up and recovered 20 HP!
Jesse reloaded 3 bullets!
Jesse
 HP: 100
 Bullets: 6
Walt
 HP: 90
 Bullets: 5
*/

// console.log();
//
// solve(([
//     "2",
//     "Gus 100 4",
//     "Walt 100 5",
//     "FireShot - Gus - Bandit",
//     "TakeHit - Walt - 100 - Bandit",
//     "Reload - Gus",
//     "Ride Off Into Sunset"
// ]));
// /*
// Gus has successfully hit Bandit and now has 3 bullets!
// Walt was gunned down by Bandit!
// Gus reloaded 3 bullets!
// Gus
//  HP: 100
//  Bullets: 6
// */