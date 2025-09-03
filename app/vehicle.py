from dataclasses import dataclass
from datetime import date
from abc import ABC, abstractmethod

@dataclass
class Vehicle(ABC):
  name: str
  year: int
  colour: str

  def age(self) -> int:
    return date.today().year - self.year
