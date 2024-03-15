num_pieces = int(input())
musical_pieces = {}

for piece, composer, key in musical_pieces:
    composer = musical_pieces['composer']
    key = musical_pieces['key']
    print(f"{piece} -> Composer: {composer}, Key: {key}")

for piece_index in range(num_pieces):
    piece, composer, key = input().split("|")

    if piece not in musical_pieces:
        musical_pieces[piece] = musical_pieces.get(piece, {'composer': composer, 'key': key})

command = input()

while command != "Stop":
    command_info = command.split("|")
    action = command_info[0]

    if action == "Add":
        piece = command_info[1]
        composer = command_info[2]
        key = command_info[3]
        if piece not in musical_pieces:
            musical_pieces[piece] = musical_pieces.get(piece, {'composer': composer, 'key': key})
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    elif action == "Remove":
        piece = command_info[1]

        if piece in musical_pieces:
            del musical_pieces[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif action == "ChangeKey":
        piece = command_info[1]
        new_key = command_info[2]

        if piece in musical_pieces:
            musical_pieces[piece]['key'] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    command = input()

for piece, value in musical_pieces.items():
    print(f"{piece} -> Composer: {value['composer']}, Key: {value['key']}")
