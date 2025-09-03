from app.inventory import Inventory
from app.settings import Settings

if __name__ == "__main__":
  print('Launching script...')
  inv = Inventory()

  inv.add_car("Seat Ibiza", 1999, 4999, "red")
  inv.add_car("Ford Fiesta", 2004, 8999, "blue")

  result = inv.all()

  print(f'Discount value: {Settings.DISCOUNT}')

  inv.apply_discount_by_name("Seat Ibiza", int(Settings.DISCOUNT))

  for car in result:
    print(f'Car name: {car.name} Year: {car.year} Price: {car.price_pence} Colour: {car.colour}')

    print(f'Car age: {car.age()} years old!')

  print('Exiting script...')