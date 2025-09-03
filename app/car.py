from dataclasses import dataclass
from app.vehicle import Vehicle

@dataclass
class Car(Vehicle):
    price_pence: int

    def apply_percentage_discount(self, percent: int) -> None:
        if not (0 <= percent <= 100):
            raise ValueError("percent must be 0..100")
        self.price_pence -= (self.price_pence * percent) // 100
