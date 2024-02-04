class Client:
    def __init__(self, phone_number: str) -> None:
        self.phone_number = phone_number

        self.shopping_cart: list = []
        self.bill: float = 0.0

    @property
    def phone_number(self):
        return self.__phone_number

    # TODO TEST IF THE VALUE ERROR WORKS CORRECTLY
    @phone_number.setter
    def phone_number(self, value):
        if len(value) != 10 or not value.startswith("0") or not value.isdigit():
            raise ValueError("Invalid phone number!")

        self.__phone_number = value
