import math
from typing import List


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages

        self.photos: List[List[str]] = self.__init_photos()
        self.current_row = 0

    def __init_photos(self):
        matrix = []

        for _ in range(self.pages):
            matrix.append([])

        return matrix

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = math.ceil(photos_count / 4)

        return cls(pages)

    def add_photo(self, label: str):
        if len(self.photos[self.current_row]) == 4:
            self.current_row += 1

        try:
            self.photos[self.current_row].append(label)

            return f"{label} photo added successfully on page {self.current_row + 1} " \
                   f"slot {len(self.photos[self.current_row])}"
        except IndexError:
            return "No more free slots"

    def display(self):
        result = "-" * 11 + '\n'

        for page in self.photos:
            result += ' '.join(['[]' for _ in page]) + '\n'
            result += "-" * 11 + '\n'

        return result


album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.display())
