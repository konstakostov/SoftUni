# The height & width of the room is entered via console in meters.
# With * 100 we turn the size from m to cm
height = float(input()) * 100
width = float(input()) * 100

# The width of the corridor in the middle is removed from the total usable width of the room,
width_with_corridor = width - 100

# The width (70) and the height (120) from each seat is divided from the user defined values.
# That way we can determine the amount of seats can be put per row and per column.
width_for_seats = width_with_corridor // 70
height_for_seats = height // 120

# We determine the amount of seats by multiplication of the available seat width and height.
# We remove 3 from the total equation because these are the number of desks we lose from the door and desk.
amount_of_seats = (width_for_seats * height_for_seats) - 3

# We print the final result - amount of seats available in the room.
print(amount_of_seats)
