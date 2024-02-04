from typing import List
from project import Product


class ProductRepository:
    def __init__(self) -> None:
        self.products: List[Product] = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> str or None:
        result = [p for p in self.products if p.name == product_name]

        if result:
            return result[0]

    def remove(self, product_name):
        product = self.find(product_name)

        if product:
            self.products.remove(product)

    def __repr__(self):
        return '\n'.join([f"{p.name}: {p.quantity}" for p in self.products])

