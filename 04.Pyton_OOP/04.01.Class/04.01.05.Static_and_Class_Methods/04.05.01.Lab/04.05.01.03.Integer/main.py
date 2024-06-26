import math


class Integer:
    def __init__(self, value: int) -> None:
        self.value = value

    @classmethod
    def from_float(cls, float_value: float):
        if not isinstance(float_value, float):
            return "value is not a float"

        return cls(math.floor(float_value))

    @classmethod
    def from_roman(cls, value: str):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40,
                 'XC': 90, 'CD': 400, 'CM': 900}

        i = 0
        num = 0

        while i < len(value):
            if i + 1 < len(value) and value[i:i + 2] in roman:
                num += roman[value[i:i + 2]]
                i += 2

            else:
                num += roman[value[i]]
                i += 1

        return cls(num)

    @classmethod
    def from_string(cls, value: str):
        if not isinstance(value, int):
            return "wrong type"

        return cls(value)
