from collections import deque


def list_manipulator(nums, *args):
    num_list = deque(nums)
    arguments = deque(args)

    command = arguments.popleft()
    position = arguments.popleft()

    if command == "add" and position == "beginning":
        arguments.reverse()

        for arg in arguments:
            num_list.appendleft(arg)

        return list(num_list)

    elif command == "add" and position == "end":
        for arg in arguments:
            num_list.append(arg)

        return list(num_list)

    elif command == "remove" and position == "beginning":
        if arguments:
            for _ in range(arguments[0]):
                if num_list:
                    num_list.popleft()
        else:
            num_list.popleft()

        return list(num_list)

    elif command == "remove" and position == "end":
        if arguments:
            for _ in range(arguments[0]):
                if num_list:
                    num_list.pop()
        else:
            num_list.pop()

        return list(num_list)


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
