spell = input()

command = input()
while command != "Abracadabra":
    info = command.split()

    if info[0] == "Abjuration":
        spell = spell.upper()
        print(spell)

    elif info[0] == "Necromancy":
        spell = spell.lower()
        print(spell)

    elif info[0] == "Illusion":
        index = int(info[1])
        letter = info[2]

        if 0 <= index < len(spell):
            spell = spell.replace(spell[index], letter, 1)
            print("Done!")
        else:
            print("The spell was too weak.")

    elif info[0] == "Divination":
        first_substring = info[1]
        second_substring = info[2]

        if first_substring in spell:
            spell = spell.replace(first_substring, second_substring)
            print(spell)
        else:
            continue

    elif info[0] == "Alteration":
        substring = info[1]

        if substring in spell:
            spell = spell.replace(substring, "")
            print(spell)
        else:
            continue

    else:
        print("The spell did not work!")

    command = input()
