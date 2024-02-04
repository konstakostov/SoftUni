to_do_notes = [0] * 10

while True:
    command = input()

    if command == "End":
        break

    importance, task = command.split("-")
    importance = int(importance) - 1

    to_do_notes[importance] = task

to_do_notes = [note for note in to_do_notes if note != 0]

print(to_do_notes)
