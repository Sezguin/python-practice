## Encapsulation

Bundle data + methods together in a class. Control access to “private” stuff.

```
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private (name-mangled)

    def deposit(self, amount):     # public method
        self.__balance += amount

    def get_balance(self):         # controlled access
        return self.__balance

acc = BankAccount(100)
acc.deposit(50)
print(acc.get_balance())  # ✅ 150
# print(acc.__balance)    # ❌ error (private)
```

## Abstraction

Hide the “how,” only show the “what.”

```
from abc import ABC, abstractmethod

class Shape(ABC):                  # abstract base class
    @abstractmethod
    def area(self):                 # must be implemented
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r * self.r

s = Circle(5)
print(s.area())   # 78.5
```

## Polymorphism

Different classes respond to the same method in different ways.

```
class Dog:
    def speak(self):
        return "Woof"

class Cat:
    def speak(self):
        return "Meow"

for animal in [Dog(), Cat()]:
    print(animal.speak())
```

Vehicle = Car or Bike

vehicle.wheels = 2 or 4 depending on object