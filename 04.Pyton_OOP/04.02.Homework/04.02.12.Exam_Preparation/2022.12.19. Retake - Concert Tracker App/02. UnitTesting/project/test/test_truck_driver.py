from project.truck_driver import TruckDriver
from unittest import TestCase, main


class TestTruckDriver(TestCase):
    def setUp(self) -> None:
        self.driver = TruckDriver("Jose", 1)

    def test__init__(self):
        self.assertEqual("Jose", self.driver.name)
        self.assertEqual(0.5, self.driver.money_per_mile)
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)

    def test_getter_setter_earned_money_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money = -1

        expected = "Jose went bankrupt."

        self.assertEqual(expected, str(ve.exception))

    def test_cargo_offer_exception(self):
        self.driver.available_cargos = {"Sofia": 100,
                                        "Plovdiv": 200,
                                        "Burgas": 300
                                        }

        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("Plovdiv", 200)

        expected = "Cargo offer is already added."

        self.assertEqual(expected, str(ex.exception))

    def test_cargo_offer_valid(self):
        self.driver.available_cargos = {"Sofia": 100,
                                        "Plovdiv": 200,
                                        "Burgas": 300
                                        }

        expected = "Cargo for 400 to Varna was added as an offer."
        result = self.driver.add_cargo_offer("Varna", 400)

        self.assertEqual(expected, result)

        expected_cargo = {"Sofia": 100,
                          "Plovdiv": 200,
                          "Burgas": 300,
                          "Varna": 400
                          }

        self.assertEqual(expected_cargo, self.driver.available_cargos)

    def test_drive_best_cargo_offer_value_error(self):
        expected = "There are no offers available."
        result = self.driver.drive_best_cargo_offer()

        self.assertEqual(expected, result)

    def test_drive_best_cargo_offer_valid(self):
        self.driver.available_cargos = {"Sofia": 100,
                                        "Plovdiv": 200,
                                        "Burgas": 300
                                        }

        expected = "Jose is driving 300 to Burgas."
        result = self.driver.drive_best_cargo_offer()

        self.assertEqual(expected, result)

        self.assertEqual(280, self.driver.earned_money)
        self.assertEqual(300, self.driver.miles)

    def test_eat(self):
        self.driver.available_cargos = {"Sofia": 250}

        self.driver.drive_best_cargo_offer()

        self.assertEqual(230, self.driver.earned_money)

    def test_sleep(self):
        self.driver.available_cargos = {"Sofia": 1000}

        self.driver.drive_best_cargo_offer()

        self.assertEqual(875, self.driver.earned_money)

    def test_pump_gas(self):
        self.driver.available_cargos = {"Sofia": 1500}

        self.driver.drive_best_cargo_offer()

        self.assertEqual(835, self.driver.earned_money)

    def test_repair_truck(self):
        self.driver.money_per_mile = 10
        self.driver.available_cargos = {"Sofia": 10000}

        self.driver.drive_best_cargo_offer()

        self.assertEqual(88250, self.driver.earned_money)

    def test__repr__(self):
        self.driver.miles = 500

        expected = "Jose has 500 miles behind his back."
        result = self.driver.__repr__()

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
