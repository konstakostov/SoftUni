# # 01. Storage
# class Storage:
#     storage = []
#
#     def __init__(self, capacity):
#         self.capacity = capacity
#
#     def add_product(self, product: str):
#         if self.capacity > 0:
#             Storage.storage.append(product)
#             self.capacity -= 1
#
#     def get_products(self):
#         return Storage.storage
#


# # 02. Weapon
# class Weapon:
#
#     def __init__(self, bullets: int):
#         self.bullets = bullets
#
#     def shoot(self):
#         if self.bullets > 0:
#             self.bullets -= 1
#             return "shooting..."
#         return "no bullets left"
#
#     def __repr__(self):
#         return f"Remaining bullets: {self.bullets}"
#


# # 03. Catalogue
# class Catalogue:
#
#     def __init__(self, name: str):
#         self.name = name
#         self.products = []
#
#     def add_product(self, product_name: str):
#         self.products.append(product_name)
#
#     def get_by_letter(self, first_letter: str):
#         return [item for item in self.products if item.startswith(first_letter)]
#
#     def __repr__(self):
#         return f"Items in the {self.name} catalogue:\n" + '\n'.join(sorted(self.products))
#


# 04. Town
# class Town:
#
#     def __init__(self, name: str, latitude="0°N", longitude="0°E"):
#         self.name = name
#         self.latitude = latitude
#         self.longitude = longitude
#
#     def set_latitude(self, latitude):
#         self.latitude = latitude
#
#     def set_longitude(self, longitude):
#         self.longitude = longitude
#
#     def __repr__(self):
#         return f"Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}"
#


# 05. Class


# 06. Inventory


# 07. Articles


# 08. *Vehicle


# 09. *Movie

