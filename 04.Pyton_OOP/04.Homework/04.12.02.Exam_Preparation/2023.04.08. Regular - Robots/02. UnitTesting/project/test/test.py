from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TestTennisPlayer(TestCase):
    def setUp(self) -> None:
        self.player = TennisPlayer("John", 33, 250)

    def test__init__(self):
        self.assertEqual("John", self.player.name)
        self.assertEqual(33, self.player.age)
        self.assertEqual(250, self.player.points)
        self.assertEqual([], self.player.wins)

    def test_getter_setter_name_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = ""

        expected = "Name should be more than 2 symbols!"

        self.assertEqual(expected, str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.player.name = "a"

        expected = "Name should be more than 2 symbols!"

        self.assertEqual(expected, str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.player.name = "aa"

        self.assertEqual(expected, str(ve.exception))

    def test_getter_setter_name_age_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.player.age = 17

        expected = "Players must be at least 18 years of age!"

        self.assertEqual(expected, str(ve.exception))

    def test_add_New_win_successfully(self):
        self.player.wins = ["WON"]

        self.player.add_new_win("NEW")

        self.assertEqual(["WON", "NEW"], self.player.wins)

    def test_add_new_win_has_been_added_to_list(self):
        self.player.wins = ["WON"]

        expected = "WON has been already added to the list of wins!"
        result = self.player.add_new_win("WON")

        self.assertEqual(expected, result)

    def test__lt__other_player_is_better(self):
        self.player = TennisPlayer("John", 33, 250)
        self.other_player = TennisPlayer("Jack", 33, 251)

        expected = "Jack is a top seeded player and he/she is better than John"
        result = self.player.__lt__(self.other_player)

        self.assertEqual(expected, result)

    def test__lt__self_player_is_better(self):
        self.player = TennisPlayer("John", 33, 250)
        self.other_player = TennisPlayer("Jack", 33, 249)

        expected = "John is a better player than Jack"
        result = self.player.__lt__(self.other_player)

        self.assertEqual(expected, result)

    def test__str__(self):
        self.player.add_new_win("NEW")
        self.player.add_new_win("WON")

        expected = "Tennis Player: John\n" \
                   "Age: 33\n" \
                   "Points: 250.0\n" \
                   "Tournaments won: NEW, WON"

        result = self.player.__str__()

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
