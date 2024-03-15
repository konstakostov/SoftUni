class Cat:
    def __init__(self, name):
        self.name = name

        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


import unittest


class CatTests(unittest.TestCase):
    def setUp(self) -> None:
        self.cat = Cat("Test")

    def test_initialised_cat(self):

        self.assertEqual("Test", self.cat.name)
        self.assertFalse(self.cat.sleepy)
        self.assertFalse(self.cat.fed)
        self.assertEqual(0, self.cat.size)

    def test_cat_eats(self):
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

        self.cat.eat()

        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(1, self.cat.size)

    def test_cat_has_eaten_raises(self):
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

        # Arrange
        self.cat.eat()

        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(1, self.cat.size)

        # Act
        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))

        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(1, self.cat.size)

    def test_cat_tries_to_sleep_cat_is_not_fed_raises(self):
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)

    def test_cat_is_not_hungry_can_go_to_sleep(self):
        self.cat.eat()

        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)

        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    unittest.main()

