from app.cars import CarClass

if __name__ == "__main__":
  print('Launching script...')
  car_class = CarClass()

  car_class.add_car("Seat Ibiza", 1999, 4999, "red")
  car_class.add_car("Ford Fiesta", 2004, 8999, "blue")

  result = car_class.get_all_cars()

  car_class.update_car_price("Seat Ibiza")

  for car in result:
    print(f'Car name: {car.name} Year: {car.year} Price: {car.price_pence} Colour: {car.colour}')

  print('Exiting script...')