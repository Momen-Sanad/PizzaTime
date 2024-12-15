from pizza import Pizza

class ToppingDecorator(Pizza):
    def __init__(self, pizza: Pizza):
        self._pizza = pizza

    def get_description(self) -> str:
        return self._pizza.get_description()

    def get_cost(self) -> float:
        return self._pizza.get_cost()

class Cheese(ToppingDecorator):
    def get_description(self) -> str:
        return f"{self._pizza.get_description()}, Cheese"

    def get_cost(self) -> float:
        return self._pizza.get_cost() + 1.0

class Olives(ToppingDecorator):
    def get_description(self) -> str:
        return f"{self._pizza.get_description()}, Olives"

    def get_cost(self) -> float:
        return self._pizza.get_cost() + 0.5

class Mushrooms(ToppingDecorator):
    def get_description(self) -> str:
        return f"{self._pizza.get_description()}, Mushrooms"

    def get_cost(self) -> float:
        return self._pizza.get_cost() + 0.7