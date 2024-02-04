from project.toy_store import ToyStore
from unittest import TestCase, main


class TestToyStore(TestCase):
    def setUp(self) -> None:
        self.store = ToyStore()

    def test__init__(self):
        expected = {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None}
        self.assertEqual(expected, self.store.toy_shelf)

    def test_add_toy_successfully(self):
        result = self.store.add_toy("A", "Toy")
        expected = "Toy:Toy placed successfully!"

        self.assertEqual(expected, result)

        expected_shelf = {'A': 'Toy', 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None}
        self.assertEqual(expected_shelf, self.store.toy_shelf)

    def test_add_toy_exception_shelf_does_not_exist(self):
        expected = "Shelf doesn't exist!"

        with self.assertRaises(Exception) as ex:
            self.store.add_toy("Z", "Toy")

        self.assertEqual(expected, str(ex.exception))

    def test_add_toy_exception_toy_is_on_shelf(self):
        self.store.add_toy("A", "Toy")

        expected = "Toy is already in shelf!"

        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "Toy")

        self.assertEqual(expected, str(ex.exception))

    def test_add_toy_exception_shelf_is_taken(self):
        self.store.add_toy("A", "Toy")

        expected = "Shelf is already taken!"

        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "OtherToy")

        self.assertEqual(expected, str(ex.exception))

    def test_remove_toy_successfully(self):
        self.store.add_toy("A", "Toy")

        result = self.store.remove_toy("A", "Toy")
        expected = "Remove toy:Toy successfully!"

        self.assertEqual(expected, result)

        expected_shelf = {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None}
        self.assertEqual(expected_shelf, self.store.toy_shelf)

    def test_remove_toy_exception_shelf_does_not_exist(self):
        self.store.add_toy("A", "Toy")

        expected = "Shelf doesn't exist!"

        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("Z", "Toy")

        self.assertEqual(expected, str(ex.exception))

    def test_remove_toy_exception_toy_does_not_exist_on_shelf(self):
        self.store.add_toy("A", "Toy")

        expected = "Toy in that shelf doesn't exists!"

        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("A", "OtherToy")

        self.assertEqual(expected, str(ex.exception))


if __name__ == "__main__":
    main()
