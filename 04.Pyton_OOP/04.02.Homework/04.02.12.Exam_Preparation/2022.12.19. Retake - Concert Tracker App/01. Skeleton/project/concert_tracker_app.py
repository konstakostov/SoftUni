from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIANS = ["Guitarist", "Drummer", "Singer"]

    def __init__(self):
        self.bands: list = []
        self.musicians: list = []
        self.concerts: list = []

    def __find_musician_by_name(self, name: str):
        for musician in self.musicians:
            if musician.name == name:
                return musician

    def __find_band_by_name(self, name: str):
        for band in self.bands:
            if band.name == name:
                return band

    def __find_concert_by_place(self, place: str):
        for concert in self.concerts:
            if concert.place == place:
                return concert

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIANS:
            raise ValueError("Invalid musician type!")

        musician = self.__find_musician_by_name(name)

        if musician:
            raise Exception(f"{name} is already a musician!")

        new_musician = None

        if musician_type == "Guitarist":
            new_musician = Guitarist(name, age)

        elif musician_type == "Drummer":
            new_musician = Drummer(name, age)

        elif musician_type == "Singer":
            new_musician = Singer(name, age)

        self.musicians.append(new_musician)

        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        band = self.__find_band_by_name(name)

        if band:
            raise Exception(f"{name} band is already created!")

        new_band = Band(name)

        self.bands.append(new_band)

        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert = self.__find_concert_by_place(place)

        if concert:
            raise Exception(f"{concert.place} is already registered for {concert.genre} concert!")

        new_concert = Concert(genre, audience, ticket_price, expenses, place)

        self.concerts.append(new_concert)

        return f"{new_concert.genre} concert in {new_concert.place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = self.__find_musician_by_name(musician_name)
        band = self.__find_band_by_name(band_name)

        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")

        if not band:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)

        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        musician = self.__find_musician_by_name(musician_name)
        band = self.__find_band_by_name(band_name)

        if not band:
            raise Exception(f"{band_name} isn't a band!")

        if musician not in band.members:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)

        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = self.__find_band_by_name(band_name)
        concert = self.__find_concert_by_place(concert_place)

        for musician_type in self.VALID_MUSICIANS:
            if not any(filter(lambda m: m.__class__.__name__ == musician_type, band.members)):
                raise Exception(f"{band.name} can't start the concert because it doesn't have enough members!")

        if concert.genre == "Rock":
            for member in band.members:
                if (member.__class__.__name__ == "Drummer" and
                        "play the drums with drumsticks" not in member.skills):
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

                if (member.__class__.__name__ == "Singer" and
                        "sing high pitch notes" not in member.skills):
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

                if (member.__class__.__name__ == "Guitarist" and
                        "play rock" not in member.skills):
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == "Metal":
            for member in band.members:
                if (member.__class__.__name__ == "Drummer" and
                        "play the drums with drumsticks" not in member.skills):
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

                if (member.__class__.__name__ == "Singer" and
                        "sing low pitch notes" not in member.skills):
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

                if (member.__class__.__name__ == "Guitarist" and
                        "play metal" not in member.skills):
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == "Jazz":
            for member in band.members:
                if (member.__class__.__name__ == "Drummer" and
                        "play the drums with drum brushes" not in member.skills):
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

                if (member.__class__.__name__ == "Singer" and
                        ("sing high pitch notes" or "sing low pitch notes")not in member.skills):
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

                if (member.__class__.__name__ == "Guitarist" and
                        "play jazz" not in member.skills):
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses

        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."
