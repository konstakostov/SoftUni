electrons = int(input())

left_electrons = electrons

filled_shells = []

current_shell = 1

while True:
    fill_shell = 2 * (current_shell ** 2)

    left_electrons -= fill_shell

    if left_electrons < 0:
        filled_shells.append(left_electrons + fill_shell)
        break
    elif left_electrons == 0:
        filled_shells.append(fill_shell)
        break
    else:
        filled_shells.append(fill_shell)
        current_shell += 1

print(filled_shells)
