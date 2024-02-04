from project.band_members.musician import Musician


class Guitarist(Musician):
    SKILLS: list = ["play metal",
                    "play rock",
                    "play jazz"
                    ]

    def __init__(self, name: str, age: int):
        super().__init__(name, age)

        self.skills: list = []

    def learn_new_skill(self, new_skill: str):
        if new_skill not in self.SKILLS:
            raise ValueError(f"{new_skill} is not a needed skill!")

        if new_skill in self.skills:
            raise Exception(f"{new_skill} is already learned!")

        self.skills.append(new_skill)

        return f"{self.name} learned to {new_skill}."
