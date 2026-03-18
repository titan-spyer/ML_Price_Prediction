from abc import ABC, abstractmethod

class Coffee(ABC):
    @abstractmethod
    def prepair(self):
        pass

class Espresso(Coffee):
    def prepair(self):
        return "Espresso"

class Americano(Coffee):
    def prepair(self):
        return "Americano"

class Cappuccino(Coffee):
    def prepair(self):
        return "Cappuccino"

class Latte(Coffee):
    def prepair(self):
        return "Latte"


class CoffeeFactory:
    def create_coffee(self, coffee_type):
        if coffee_type == "espresso":
            return Espresso().prepair()
        elif coffee_type == "americano":
            return Americano().prepair()
        elif coffee_type == "cappuccino":
            return Cappuccino().prepair()
        elif coffee_type == "latte":
            return Latte().prepair()
        else:
            return None

if __name__ == "__main__":
    factory = CoffeeFactory()
    coffee = factory.create_coffee("espresso")
    print(coffee)
    coffee = factory.create_coffee("americano")
    print(coffee)
    coffee = factory.create_coffee("cappuccino")
    print(coffee)
    coffee = factory.create_coffee("latte")
    print(coffee)
    coffee = factory.create_coffee("invalid")
    print(coffee)