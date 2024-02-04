from project.shopping_cart import ShoppingCart
from unittest import TestCase, main


class TestShoppingCart(TestCase):
    def setUp(self) -> None:
        self.cart = ShoppingCart("Shop", 50)

    def test__init__(self):
        self.assertEqual("Shop", self.cart.shop_name)
        self.assertEqual(50, self.cart.budget)
        self.assertEqual({}, self.cart.products)

    def test_shop_name_getter_setter_valid(self):
        self.assertEqual("Shop", self.cart.shop_name)

    def test_shop_name_getter_setter_invalid(self):
        with self.assertRaises(ValueError) as ve:
            ShoppingCart("Sh0p", 50)

        expected = "Shop must contain only letters and must start with capital letter!"

        self.assertEqual(expected, str(ve.exception))

    def test_add_to_cart_valid(self):
        self.cart.add_to_cart("Bear", 25)

        expected_message = "Bear product was successfully added to the cart!"
        result_message = self.cart.add_to_cart("Bear", 25)
        self.assertEqual(expected_message, result_message)

        expected_cart = {"Bear": 25}
        result_cart = self.cart.products
        self.assertEqual(expected_cart, result_cart)

    def test_add_to_cart_invalid(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.add_to_cart("Bear", 100)

        expected = "Product Bear cost too much!"

        self.assertEqual(expected, str(ve.exception))

    def test_remove_from_card_valid(self):
        self.cart.add_to_cart("Bear", 25)
        self.cart.add_to_cart("Wolf", 15)

        expected_message = "Product Bear was successfully removed from the cart!"
        result_message = self.cart.remove_from_cart("Bear")
        self.assertEqual(expected_message, result_message)

        expected_cart = {"Wolf": 15}
        result_cart = self.cart.products
        self.assertEqual(expected_cart, result_cart)

    def test_remove_from_card_invalid(self):
        self.cart.add_to_cart("Bear", 25)
        self.cart.add_to_cart("Wolf", 15)

        with self.assertRaises(ValueError) as ve:
            self.cart.remove_from_cart("Horse")

        expected = "No product with name Horse in the cart!"

        self.assertEqual(expected, str(ve.exception))

    def test__add__(self):
        first_cart = ShoppingCart("First", 50)
        first_cart.add_to_cart("For_First", 10)

        second_cart = ShoppingCart("Second", 75)
        second_cart.add_to_cart("For_Second", 10)

        merged = first_cart.__add__(second_cart)

        self.assertEqual("FirstSecond", merged.shop_name)
        self.assertEqual(125, merged.budget)
        self.assertEqual({"For_First": 10, "For_Second": 10}, merged.products)

    def test_buy_products_valid(self):
        self.cart.add_to_cart("Bear", 25)
        self.cart.add_to_cart("Wolf", 15)

        self.cart.buy_products()

        expected = 'Products were successfully bought! Total cost: 40.00lv.'
        result = self.cart.buy_products()

        self.assertEqual(expected, result)

    def test_buy_products_invalid(self):
        self.cart.add_to_cart("Bear", 25)
        self.cart.add_to_cart("Wolf", 15)
        self.cart.add_to_cart("Fox", 20)

        with self.assertRaises(ValueError) as ve:
            self.cart.buy_products()

        expected = "Not enough money to buy the products! Over budget with 10.00lv!"

        self.assertEqual(expected, str(ve.exception))


if __name__ == "__main__":
    main()
