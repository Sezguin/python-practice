from typing import Optional
from app.vehicle import Vehicle
from app.car import Car

class Inventory:
    def __init__(self) -> None:
        self._items: list[Vehicle] = []

    def add_car(self, name: str, year: int, price_pence: int, colour: str) -> Car:
        car = Car(name=name, year=year, price_pence=price_pence, colour=colour)
        self._items.append(car)
        return car

    def add(self, vehicle: Vehicle) -> Vehicle:
        self._items.append(vehicle)
        return vehicle

    def all(self) -> list[Vehicle]:
        return self._items

    def find(self, name: str) -> Optional[Vehicle]:
        return next((v for v in self._items if v.name == name), None)

    def apply_discount_by_name(self, name: str, percent: int) -> int:
        if not (0 <= percent <= 100):
            raise ValueError("percent must be 0..100")
        updated = 0
        for v in self._items:
            if isinstance(v, Car) and v.name == name:
                v.apply_percentage_discount(percent)
                updated += 1
        if updated == 0:
            raise LookupError(f"No car found with name {name!r}")
        return updated
