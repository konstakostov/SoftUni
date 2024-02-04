from unittest import TestCase, main
from project.movie import Movie


class TestMovie(TestCase):
    def setUp(self) -> None:
        self.movie = Movie("The Movie", 2023, 9.50)

    def test_correct_init(self):
        self.assertEqual("The Movie", self.movie.name)
        self.assertEqual(2023, self.movie.year)
        self.assertEqual(9.50, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_set_name_to_empty_string_raising_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.movie.name = ""

        self.assertEqual(
            "Name cannot be an empty string!",
            str(ex.exception)
        )

    def test_set_year_to_or_before_1886_raising_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.movie.year = 1886

        self.assertEqual(
            "Year is not valid!",
            str(ex.exception)
        )

    def test_add_unique_actor_to_the_actor_list(self):
        self.assertEqual([], self.movie.actors)
        self.movie.add_actor("John Smith")
        self.assertEqual(["John Smith"], self.movie.actors)

    def test_add_existing_actor_to_the_actor_list(self):
        self.movie.add_actor("John Smith")
        result = self.movie.add_actor("John Smith")

        self.assertEqual(
            f"John Smith is already added in the list of actors!",
            result)

    def test_first_movie_rating_is_better_than_second_movie_rating(self):
        new_movie = Movie("The Other Movie", 2022, 9.00)
        result = self.movie > new_movie

        self.assertEqual(
            f'"The Movie" is better than "The Other Movie"',
            result)

    def test_second_movie_rating_is_better_than_first_movie_rating(self):
        new_movie = Movie("The Other Movie", 2022, 10.00)
        result = new_movie > self.movie

        self.assertEqual(
            '"The Other Movie" is better than "The Movie"',
            result
        )

    def test__repr__(self):
        self.movie.add_actor("John Smith")
        self.movie.add_actor("Jane Doe")

        expected = f"Name: The Movie\n" \
                   f"Year of Release: 2023\n" \
                   f"Rating: 9.50\n" \
                   f"Cast: John Smith, Jane Doe"

        result = self.movie.__repr__()

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
