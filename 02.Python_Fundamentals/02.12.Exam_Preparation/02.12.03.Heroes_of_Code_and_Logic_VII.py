num_heroes = int(input())
heroes = {}

for _ in range(num_heroes):
    name, hit_points, mana_points = input().split()
    heroes[name] = heroes.get(name, {'hit_points': int(hit_points), 'mana_points': int(mana_points)})

while True:
    command = input()
    if command == "End":
        break

    info = command.split(" - ")

    if info[0] == "CastSpell":
        name = info[1]
        mana_points_needed = int(info[2])
        spell = info[3]

        if heroes[name]['mana_points'] >= mana_points_needed:
            heroes[name]['mana_points'] -= mana_points_needed
            print(f"{name} has successfully cast {spell} and now has {heroes[name]['mana_points']} MP!")
        else:
            print(f"{name} does not have enough MP to cast {spell}!")

    elif info[0] == "TakeDamage":
        name = info[1]
        damage = int(info[2])
        attacker = info[3]

        heroes[name]['hit_points'] -= damage

        if heroes[name]['hit_points'] > 0:
            print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes[name]['hit_points']} HP left!")
        else:
            del heroes[name]
            print(f"{name} has been killed by {attacker}!")

    elif info[0] == "Recharge":
        name = info[1]
        amount = int(info[2])

        heroes[name]['mana_points'] += amount
        if heroes[name]['mana_points'] <= 200:
            print(f"{name} recharged for {amount} MP!")
        else:
            amount -= (heroes[name]['mana_points'] - 200)
            print(f"{name} recharged for {amount} MP!")
            heroes[name]['mana_points'] = 200

    elif info[0] == "Heal":
        name = info[1]
        amount = int(info[2])

        heroes[name]['hit_points'] += amount
        if heroes[name]['hit_points'] <= 100:
            print(f"{name} healed for {amount} HP!")
        else:
            amount -= (heroes[name]['hit_points'] - 100)
            print(f"{name} healed for {amount} HP!")
            heroes[name]['hit_points'] = 100

for hero, status in heroes.items():
    print(hero)
    print(f"  HP: {status['hit_points']}")
    print(f"  MP: {status['mana_points']}")
