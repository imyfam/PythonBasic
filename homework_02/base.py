from abc import ABC
from homework_02.exceptions import LowFuelError
from homework_02.exceptions import NotEnoughFuel


class Vehicle(ABC):
    weight = 100
    started = False
    fuel = 0
    fuel_consumption = 0
    distance = 0


    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError("Нет топлива для запуска двигателя")

    def move(self, distance):
        self.distance = distance
        estimate_fuel_needs = self.distance * self.fuel_consumption
        if self.fuel >= estimate_fuel_needs:
            self.fuel = self.fuel - estimate_fuel_needs
        else:
            raise NotEnoughFuel("Не достаточно топлива для преодоления заданной дистанций")


# car_3 = Vehicle(1200, 5, 7)
# # car_3.fuel_consumption = 7
# # car_3.fuel = 4.2
# # print(car_3.fuel, car_3.fuel_consumption, car_3.distance)
# # car_3.move(61)
# # print(car_3.fuel, car_3.fuel_consumption, car_3.distance)
# # print((60 * 7)/100)



# print(car_3.distance)
# try:
#     car_3.move(1)
# except NotEnoughFuel as n:
#     print(n)
#
# print(car_3.fuel, car_3.fuel_consumption, car_3.distance)


# car_2 = Vehicle(1000, 0, '7na100')
# car_2.distance = 23
# print("Дистанция", car_2.distance)
#
# print(car_2.weight, car_2.fuel, car_2.fuel_consumption, car_2.started)
# try:
#     car_2.start()
# except LowFuelError as e:
#     print(e)
# print(car_2.weight, car_2.fuel, car_2.fuel_consumption, car_2.started)
