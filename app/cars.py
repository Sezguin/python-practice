from app.vehicle import Vehicle
from dataclasses import dataclass

DISCOUNT = 10

@dataclass
class Car(Vehicle):
    price_pence: int

class CarClass:
    def __init__(self) -> None:
        self._cars: list[Car] = []

    def add_car(self, name: str, year: int, price_pence: int, colour: str) -> None:
        self._cars.append(Car(name=name, year=year, price_pence=price_pence, colour=colour))

    def update_car_price(self, name: str):
        for car in self._cars:
            if car.name == name:
                new_price_pence = self.calculate_discount(car.price_pence)
                car.price_pence = new_price_pence

    def get_all_cars(self) -> list[Car]:
        return self._cars

    def get_single_car(self, car_name: str) -> Car:
        for car in self._cars:
            if car.name == car_name:
                return car

    def calculate_discount(self, price_pence: int) -> int:
        discount_percentage = DISCOUNT / 100
        money_off = price_pence * discount_percentage
        return price_pence - money_off

    def add_two_numbers_together(self, first_number:int, second_number:int) -> int:
        return first_number + second_number
