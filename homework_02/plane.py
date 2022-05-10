"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload

class Plane(Vehicle):
    cargo = 0
    max_cargo = 200000

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    # объявите метод load_cargo, который принимает число, проверяет, что в сумме с текущим cargo
    # не будет перегруза, и обновляет значение, в ином случае выкидывает исключение exceptions.CargoOverload

    def load_cargo(self, load_cargo):
        if self.max_cargo >= self.cargo + load_cargo:
            self.cargo = self.cargo + load_cargo
        else:
            raise CargoOverload("Превышение по весу")

    def remove_all_cargo(self):
        cargo_old = self.cargo
        self.cargo = 0
        return cargo_old

