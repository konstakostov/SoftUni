class Band:
    def __init__(self, name: str) -> None:
        self.name = name

        self.members: list = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Band name should contain at least one character!")

        self.__name = value

    # ADDITIONAL METHOD
    def add_members(self, musician):
        self.members.append(musician)

    # ADDITIONAL METHOD
    def remove_members(self, musician):
        self.members.remove(musician)

    def __str__(self) -> str:
        return f"{self.name} with {len(self.members)} members."
