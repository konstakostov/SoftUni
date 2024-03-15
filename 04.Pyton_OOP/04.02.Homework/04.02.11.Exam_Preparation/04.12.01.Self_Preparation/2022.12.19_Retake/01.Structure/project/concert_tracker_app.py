from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_TYPES = ["Guitarist", "Drummer", "Singer"]
    ALL_MUSICIAN_NAMES = []
    ALL_BAND_NAMES = []

    def __init__(self) -> None:
        self.bands: list = []
        self.musicians: list = []
        self.concerts: list = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in ConcertTrackerApp.VALID_TYPES:
            raise ValueError("Invalid musician type!")

        if name in ConcertTrackerApp.ALL_MUSICIAN_NAMES:
            raise Exception(f"{name} is already a musician!")

        musician = ""

        if musician_type == "Singer":
            musician = Singer(name, age)

        elif musician_type == "Drummer":
            musician = Drummer(name, age)

        elif musician_type == "Guitarist":
            musician = Guitarist(name, age)

        self.musicians.append(musician)
        self.ALL_MUSICIAN_NAMES.append(musician.name)

        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        if name in ConcertTrackerApp.ALL_BAND_NAMES:
            raise Exception(f"{name} band is already created!")

        band = Band(name)

        self.bands.append(band)
        ConcertTrackerApp.ALL_BAND_NAMES.append(band)

        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        for concert in self.concerts:
            if concert.place == place:
                return Exception(f"{place} is already registered for {genre} concert!")

        concert = Concert(genre, audience, ticket_price, expenses, place)

        self.concerts.append(concert)

        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = self._find_musician_by_name(musician_name)
        band = self._find_band_by_name(band_name)

        band.add_members(musician)

        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = self._find_band_by_name(band_name)
        musician = self._find_musician_by_name_in_band(band, musician_name)

        band.remove_members(musician)

        return f"{musician_name} was removed from {band_name}."

    # ADDITIONAL METHOD
    def _find_musician_by_name(self, musician_name: str):
        for musician in self.musicians:
            if musician.name == musician_name:
                return musician

        raise Exception(f"{musician_name} isn't a musician!")

    # ADDITIONAL METHOD
    @staticmethod
    def _find_musician_by_name_in_band(band, musician_name: str):
        for musician in band.members:
            if musician.name == musician_name:
                return musician

        raise Exception(f"{musician_name} isn't a member of {band.name}!")

    # ADDITIONAL METHOD
    def _find_band_by_name(self, band_name: str):
        for band in self.bands:
            if band.name == band_name:
                return band

        raise Exception(f"{band_name} isn't a band!")

    def start_concert(self, concert_place: str, band_name: str):
        concert = self._find_concert_by_place(concert_place)
        band = self._find_band_by_name(band_name)

        not_ready = False

        for musician_type in ConcertTrackerApp.VALID_TYPES:
            if not any(filter(lambda x: x.__class__.__name__ == musician_type, band.members)):
                raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        if concert.genre == "Rock":
            for member in band.members:
                if member.__class__.__name__ == "Drummer" and "play the drums with drumsticks" not in member.skills:
                    not_ready = True

                elif member.__class__.__name__ == "Singer" and "sing high pitch notes" not in member.skills:
                    not_ready = True

                elif member.__class__.__name__ == "Guitarist" and "play rock" not in member.skills:
                    not_ready = True

        elif concert.genre == "Metal":
            for member in band.members:
                if member.__class__.__name__ == "Drummer" and "play the drums with drumsticks" not in member.skills:
                    not_ready = True

                elif member.__class__.__name__ == "Singer" and "sing low pitch notes" not in member.skills:
                    not_ready = True

                elif member.__class__.__name__ == "Guitarist" and "play metal" not in member.skills:
                    not_ready = True

        elif concert.genre == "Jazz":
            for member in band.members:
                if member.__class__.__name__ == "Drummer" and "play the drums with drum brushes" not in member.skills:
                    not_ready = True

                elif member.__class__.__name__ == "Singer" and "sing high pitch notes" not in member.skills and \
                        "sing low pitch notes" not in member.skills:
                    not_ready = True

                elif member.__class__.__name__ == "Guitarist" and "play jazz" not in member.skills:
                    not_ready = True

        if not_ready:
            raise Exception(f"The {band_name} band is not ready to play at the concert!")

        concert_profit = (concert.audience * concert.ticket_price) - concert.expenses

        return f"{band_name} gained {concert_profit:.2f}$ from the {concert.genre} concert in {concert_place}."

    def _find_concert_by_place(self, concert_place):
        for concert in self.concerts:
            if concert.place == concert_place:
                return concert
