"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):
    engine = ''

    def set_engine(self, motor):
        self.engine = motor


# motor = Engine(3, 6)
# print(motor)
# c = Car(1200, 5, 7)
# print('parametry AVTO: ', c.weight, c.fuel, c.fuel_consumption, c.started)
# c.set_engine(motor)
# print('Novye parametry AVTO: ', c.weight, c.fuel, c.fuel_consumption, c.engine, c.started)
