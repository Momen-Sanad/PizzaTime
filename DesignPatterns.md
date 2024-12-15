# Design Patterns in Pizza Restaurant System

## Factory Pattern

**Description:**

The Factory Pattern is used to create objects without exposing the instantiation logic to the client. In the Pizza Restaurant system, this pattern is applied to create base pizzas like Margherita and Pepperoni.

### Before Applying the Pattern:

- Pizza creation logic was mixed with the main workflow, making it hard to scale or add new pizza types.

### After Applying the Pattern:

- Centralized the pizza creation logic into separate classes, improving maintainability and extensibility.

### Code Example:

```python
class Margherita(Pizza):
    def get_description(self) -> str:
        return "Margherita"

    def get_cost(self) -> float:
        return 5.0

class Pepperoni(Pizza):
    def get_description(self) -> str:
        return "Pepperoni"

    def get_cost(self) -> float:
        return 6.0
```

---

## Decorator Pattern

**Description:**

The Decorator Pattern allows behavior to be added dynamically to objects. In this system, it is used to add toppings like Cheese, Olives, and Mushrooms to pizzas.

### Before Applying the Pattern:

- Topping combinations were hardcoded, leading to duplicated code and inflexibility.

### After Applying the Pattern:

- Toppings are dynamically added as decorators, making the system more modular and flexible.

### Code Example:

```python
class Cheese(ToppingDecorator):
    def get_description(self) -> str:
        return f"{self._pizza.get_description()}, Cheese"

    def get_cost(self) -> float:
        return self._pizza.get_cost() + 1.0
```

---

## Singleton Pattern

**Description:**

The Singleton Pattern ensures only one instance of a class is created. This is applied to the `InventoryManager` to manage stock availability centrally.

### Before Applying the Pattern:

- Multiple instances of inventory management could lead to inconsistent states.

### After Applying the Pattern:

- Ensures a single source of truth for inventory, improving consistency.

### Code Example:

```python
class InventoryManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._inventory = {...}
        return cls._instance
```

---

## Overengineering

**Description:**

Overengineering occurs when unnecessary complexity is added to a system, reducing its usability and maintainability.

### Example of Overengineering:

Adding an abstract factory for pizza creation would introduce unneeded complexity for a simple system.

### Code Example (Overengineered):

```python
class AbstractPizzaFactory(ABC):
    @abstractmethod
    def create_pizza(self) -> Pizza:
        pass
```

### Why Avoid?

- Adds unnecessary abstraction for a straightforward process.
- Increases maintenance and onboarding complexity.
