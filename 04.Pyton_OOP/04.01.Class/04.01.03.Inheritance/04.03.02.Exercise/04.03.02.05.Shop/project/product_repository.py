from typing import List, Optional
from project import Product


class ProductRepository:
    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, name: str) -> Optional[Product]:
        result = [p for p in self.products if p.name == name]

        if result:
            return result[0]

    def remove(self, name: str) -> None:
        product = self.find(name)
        self.products.remove(product)

    def __repr__(self) -> str:
        return '\n'.join([f"{p.name}: {p.quantity}" for p in self.products])







