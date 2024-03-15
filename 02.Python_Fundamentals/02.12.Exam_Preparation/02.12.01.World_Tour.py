stops = input()

command = input()

while command != "Travel":
    action, param_01, param_02 = command.split(":")

    if action == "Add Stop":
        index = int(param_01)
        string_to_insert = param_02

        if 0 <= index < len(stops):
            stops = stops[:index] + string_to_insert + stops[index::]

        print(stops)

    elif action == "Remove Stop":
        start_index = int(param_01)
        end_index = int(param_02)

        if 0 <= start_index < len(stops) and 0 <= end_index < len(stops):
            stops = stops[:start_index] + stops[end_index + 1::]

        print(stops)

    elif action == "Switch":
        old_string = param_01
        new_string = param_02

        if old_string in stops:
            stops = stops.replace(old_string, new_string)

        print(stops)

    command = input()

print(f"Ready for world tour! Planned stops: {stops}")
