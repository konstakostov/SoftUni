from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    VALID_BREEDS = ["Appaloosa", "Thoroughbred"]

    def __init__(self) -> None:
        self.horses: list = []
        self.jockeys: list = []
        self.horse_races: list = []

    def _find_if_horse_exist(self, horse_type: str):
        horse = next(filter(lambda h: type(h).__name__ == horse_type and not h.is_taken, reversed(self.horses)), None)

        if not horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        return horse

    def _find_if_jockey_exist(self, jockey_name: str):
        jockey = next(filter(lambda j: j.name == jockey_name, self.jockeys), None)

        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        return jockey

    def _find_if_race_exist(self, race_type: str):
        race = next(filter(lambda r: r.race_type == race_type, self.horse_races), None)

        if not race:
            raise Exception(f"Race {race_type} could not be found!")

        return race

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type not in self.VALID_BREEDS:
            return

        if horse_name in [horse.name for horse in self.horses]:
            raise Exception(f"Horse {horse_name} has been already added!")

        new_horse = None
        if horse_type == "Appaloosa":
            new_horse = Appaloosa(horse_name, horse_speed)
        elif horse_type == "Thoroughbred":
            new_horse = Thoroughbred(horse_name, horse_speed)

        self.horses.append(new_horse)

        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if jockey_name in [jockey.name for jockey in self.jockeys]:
            raise Exception(f"Jockey {jockey_name} has been already added!")

        new_jockey = Jockey(jockey_name, age)

        self.jockeys.append(new_jockey)

        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if race_type in [race.race_type for race in self.horse_races]:
            raise Exception(f"Race {race_type} has been already created!")

        new_race = HorseRace(race_type)

        self.horse_races.append(new_race)

        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self._find_if_jockey_exist(jockey_name)
        horse = self._find_if_horse_exist(horse_type)

        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = horse
        horse.is_taken = True

        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = self._find_if_race_exist(race_type)
        jockey = self._find_if_jockey_exist(jockey_name)

        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)

        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = self._find_if_race_exist(race_type)

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner_jockey = ""
        winner_horse = ""
        top_speed = 0

        for jockey in race.jockeys:
            if jockey.horse.speed > top_speed:
                top_speed = jockey.horse.speed
                winner_jockey = jockey.name
                winner_horse = jockey.horse.name

        return (f"The winner of the {race_type} race, with a speed of "
                f"{top_speed}km/h is {winner_jockey}! Winner's horse: {winner_horse}.")
