from dataclasses import dataclass
from datetime import date

@dataclass
class Vehicle():
  name: str
  year: int
  colour: str

  def age(self) -> int:
    return date.today().year - self.year
