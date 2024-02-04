from project.robot import Robot
from unittest import TestCase, main


class TestRobot(TestCase):
    def setUp(self) -> None:
        self.robot = Robot("robot", "Military", 200, 1000)

        # self.robot.software_updates = ["update01", "update02", "update03"]

    def test__init__(self):
        self.assertEqual("robot", self.robot.robot_id)
        self.assertEqual("Military", self.robot.category)
        self.assertEqual(200, self.robot.available_capacity)
        self.assertEqual(1000, self.robot.price)

        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

    def test_getter_setter_category_valid(self):
        self.robot.category = "Military"
        self.assertEqual("Military", self.robot.category)

        self.robot.category = "Education"
        self.assertEqual("Education", self.robot.category)

        self.robot.category = "Entertainment"
        self.assertEqual("Entertainment", self.robot.category)

        self.robot.category = "Humanoids"
        self.assertEqual("Humanoids", self.robot.category)

    def test_getter_setter_category_invalid(self):
        with self.assertRaises(ValueError) as ve:
            Robot("robot", "Ivalid", 20, 1000)

        expected = "Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'"

        self.assertEqual(expected, str(ve.exception))

    def test_getter_setter_price_valid(self):
        self.robot.price = 0
        self.assertEqual(0, self.robot.price)

    def test_getter_setter_price_invalid(self):
        with self.assertRaises(ValueError) as ve:
            Robot("robot", "Military", 20, -500)

        expected = "Price cannot be negative!"

        self.assertEqual(expected, str(ve.exception))

    def test_upgrade_component_not_upgraded(self):
        self.robot.hardware_upgrades = ["upgrade01"]
        self.assertEqual(["upgrade01"], self.robot.hardware_upgrades)

        expected = "Robot robot was not upgraded."
        result = self.robot.upgrade("upgrade01", 50)

        self.assertEqual(expected, result)
        self.assertEqual(1000, self.robot.price)

    def test_upgrade_component_upgraded(self):
        self.robot.hardware_upgrades = ["upgrade01"]
        self.assertEqual(["upgrade01"], self.robot.hardware_upgrades)

        expected = 'Robot robot was upgraded with Wrench.'
        result = self.robot.upgrade("Wrench", 20)
        self.assertEqual(expected, result)
        self.assertEqual(1030, self.robot.price)
        self.assertEqual(["upgrade01", "Wrench"], self.robot.hardware_upgrades)

    def test_update_robot_was_not_updated(self):
        self.robot.software_updates = [1.2]
        self.assertEqual([1.2], self.robot.software_updates)

        expected = "Robot robot was not updated."
        result = self.robot.update(1.1, 150)

        self.assertEqual(expected, result)

        expected = "Robot robot was not updated."
        result = self.robot.update(1.4, 780)

        self.assertEqual(expected, result)

    def test_update_robot_was_updated(self):
        self.robot.software_updates = [1.2]
        self.assertEqual([1.2], self.robot.software_updates)

        expected = 'Robot robot was updated to version 1.5.'
        result = self.robot.update(1.5, 10)

        self.assertEqual(expected, result)
        self.assertEqual([1.2, 1.5], self.robot.software_updates)
        self.assertEqual(190, self.robot.available_capacity)

    def test__gt__robot_price_is_more_expensive(self):
        self.robot = Robot("mil", "Military", 150, 1500)
        self.other_robot = Robot("edu", "Education", 100, 1000)

        expected = 'Robot with ID mil is more expensive than Robot with ID edu.'
        result = self.robot > self.other_robot

        self.assertEqual(expected, result)

    def test__gt__robot_price_is_equal(self):
        self.robot = Robot("mil", "Military", 150, 1000)
        self.other_robot = Robot("edu", "Education", 100, 1000)

        expected = 'Robot with ID mil costs equal to Robot with ID edu.'
        result = self.robot > self.other_robot

        self.assertEqual(expected, result)

    def test__gt__robot_price_is_cheaper(self):
        self.robot = Robot("mil", "Military", 150, 900)
        self.other_robot = Robot("edu", "Education", 100, 1000)

        expected = 'Robot with ID mil is cheaper than Robot with ID edu.'
        result = self.robot > self.other_robot

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
