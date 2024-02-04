from project.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):
    MAX_MILEAGE = 180.00

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, max_mileage=self.MAX_MILEAGE)

    # CHECK IF METHOD MATH IS CORRECT
    def drive(self, mileage: float):
        reduce_battery_with = mileage / self.max_mileage + 0.05

        self.battery_level -= reduce_battery_with * 100

        self.battery_level = round(self.battery_level)



