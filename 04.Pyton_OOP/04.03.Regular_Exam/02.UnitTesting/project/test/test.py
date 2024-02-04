from project.second_hand_car import SecondHandCar
from unittest import TestCase, main


class TestSecondHandCar(TestCase):
    def setUp(self) -> None:
        self.car = SecondHandCar("Model", "Type", 10000, 2000)

    def test__init__(self):
        self.assertEqual("Model", self.car.model)
        self.assertEqual("Type", self.car.car_type)
        self.assertEqual(10000, self.car.mileage)
        self.assertEqual(2000, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_setter_getter_price_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 0.99

        expected = "Price should be greater than 1.0!"

        self.assertEqual(expected, str(ve.exception))

    def test_setter_getter_mileage_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 99

        expected = "Please, second-hand cars only! Mileage must be greater than 100!"

        self.assertEqual(expected, str(ve.exception))

    def test_set_promotional_price_valid(self):
        expected = "The promotional price has been successfully set."
        result = self.car.set_promotional_price(1000)

        self.assertEqual(expected, result)
        self.assertEqual(1000, self.car.price)

    def test_set_promotional_price_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(3000)

        expected = "You are supposed to decrease the price!"

        self.assertEqual(expected, str(ve.exception))
        self.assertEqual(2000, self.car.price)

    def test_need_repair_impossible(self):
        expected = "Repair is impossible!"
        result = self.car.need_repair(2000, "Description")

        self.assertEqual(expected, result)

    def test_need_repair_price_increase(self):
        expected = "Price has been increased due to repair charges."
        result = self.car.need_repair(500, "Description")

        self.assertEqual(expected, result)
        self.assertEqual(2500, self.car.price)
        self.assertEqual(["Description"], self.car.repairs)

    def test__gt__valid(self):
        self.car = SecondHandCar("Model", "Type", 10000, 3200)
        self.other_car = SecondHandCar("Model", "Type", 10000, 3100)

        self.assertTrue(self.car > self.other_car)

    def test__gt__mismatch(self):
        self.car = SecondHandCar("Model", "Type", 10000, 2000)
        self.other_car = SecondHandCar("Model", "Non-Type", 10000, 2000)

        expected = "Cars cannot be compared. Type mismatch!"
        result = self.car > self.other_car

        self.assertEqual(expected, result)

    def test_str__(self):
        self.car = SecondHandCar("Mustang", "Muscle", 15000, 12000)
        self.car.repairs = ["Changed Tires", "Upgraded Engine", "New Wipers"]

        expected = """Model Mustang | Type Muscle | Milage 15000km
Current price: 12000.00 | Number of Repairs: 3"""
        result = self.car.__str__()

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
