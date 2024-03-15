from collections import deque

sequence = deque(input())
open_parenthesis = deque()

while sequence:
    current = sequence.popleft()

    if current in "([{":
        open_parenthesis.append(current)

    elif not open_parenthesis:
        print("NO")
        break

    else:
        pair = open_parenthesis.pop() + current

        if pair not in "()[]{}":
            print("NO")
            break
else:
    print("YES")

