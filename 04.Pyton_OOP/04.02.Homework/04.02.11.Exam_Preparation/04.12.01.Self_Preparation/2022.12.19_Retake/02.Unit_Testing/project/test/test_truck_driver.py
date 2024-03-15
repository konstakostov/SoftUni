from project.truck_driver import TruckDriver
from unittest import TestCase, main


class TestTruckDriver(TestCase):
    def setUp(self) -> None:
        self.driver = TruckDriver("John", 1.50)

    def test_is_init_correct(self):
        self.assertEqual("John", self.driver.name)
        self.assertEqual(1.50, self.driver.money_per_mile)
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)

    def test_earned_money_is_valid(self):
        self.driver.earned_money = 150
        self.assertEqual(150, self.driver.earned_money)

    def test_earned_money_is_not_valid(self):
        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money = -50

        self.assertEqual("John went bankrupt.", str(ve.exception))

    def test_add_cargo_is_valid(self):
        result = self.driver.add_cargo_offer("Sofia", 150)
        expected = "Cargo for 150 to Sofia was added as an offer."

        self.assertEqual(expected, result)
        self.assertEqual(self.driver.available_cargos, {"Sofia": 150})

    def test_add_cargo_is_not_valid(self):
        self.driver.add_cargo_offer("Sofia", 150)

        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("Sofia", 150)

        expected = "Cargo offer is already added."

        self.assertEqual(expected, str(ex.exception))

    def test_drive_best_cargo_is_valid(self):
        self.assertEqual(0, self.driver.earned_money)

        self.driver.add_cargo_offer("Sofia", 150)
        self.driver.add_cargo_offer("Burgas", 400)

        result = self.driver.drive_best_cargo_offer()
        expected_str = "John is driving 400 to Burgas."
        expected_money = 580
        expected_miles = 400

        self.assertEqual(expected_str, result)
        self.assertEqual(expected_money, self.driver.earned_money)
        self.assertEqual(expected_miles, self.driver.miles)

    def test_drive_best_cargo_is_not_valid(self):
        result = self.driver.drive_best_cargo_offer()
        expected = "There are no offers available."

        self.assertEqual(expected, result)

    def test_eat_costs_money(self):
        self.driver.earned_money = 1000

        self.driver.eat(250)
        self.assertEqual(980, self.driver.earned_money)

    def test_sleep_costs_money(self):
        self.driver.earned_money = 10000

        self.driver.sleep(1000)
        self.assertEqual(9955, self.driver.earned_money)

    def test_pump_gas_costs_money(self):
        pass
        self.driver.earned_money = 10000

        self.driver.pump_gas(1500)
        self.assertEqual(9500, self.driver.earned_money)

    def test_repair_truck_costs_money(self):
        self.driver.earned_money = 10000

        self.driver.repair_truck(10000)
        self.assertEqual(2500, self.driver.earned_money)

    def test__repr__(self):
        expected = "John has 0 miles behind his back."
        result = str(self.driver)

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
