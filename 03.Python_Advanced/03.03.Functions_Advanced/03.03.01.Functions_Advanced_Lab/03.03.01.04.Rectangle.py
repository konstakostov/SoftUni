def rectangle(length, width):
    if not isinstance(length, int) or not isinstance(width, int):
        return "Enter valid values!"

    def area():
        return length * width

    def perimeter():
        return length * 2 + width * 2

    return f"Rectangle area: {area()}\n" \
           f"Rectangle perimeter: {perimeter()}"


print(rectangle(2, 10))
print(rectangle('2', 10))
