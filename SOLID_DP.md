# Mapping Design Patterns to SOLID Principles

## Factory Pattern

### Related Principles:

- **Single Responsibility Principle (SRP):** Pizza creation logic is centralized, adhering to SRP by isolating the responsibility of creating pizzas from the main workflow.
- **Open/Closed Principle (OCP):** New pizza types can be added by creating new classes without modifying existing logic.

## Decorator Pattern

### Related Principles:

- **Open/Closed Principle (OCP):** Toppings can be dynamically added without altering existing pizza classes.
- **Liskov Substitution Principle (LSP):** Decorated pizzas can replace base pizzas in the system seamlessly.

## Singleton Pattern

### Related Principles:

- **Single Responsibility Principle (SRP):** The `InventoryManager` is solely responsible for managing inventory, ensuring a single source of truth.
- **Dependency Inversion Principle (DIP):** High-level modules depend on the single instance of `InventoryManager`, avoiding direct coupling with inventory details.

---

## Summary of SOLID Principles

### Single Responsibility Principle (SRP)

Each class in the system has a well-defined responsibility, e.g., `InventoryManager` handles stock management, and `ToppingDecorator` handles topping customization.

### Open/Closed Principle (OCP)

The system is open for extension (e.g., adding new toppings or pizzas) but closed for modification.

### Liskov Substitution Principle (LSP)

Derived classes (e.g., decorators) can replace base classes (e.g., pizzas) without affecting the system.

### Dependency Inversion Principle (DIP)

Modules depend on abstractions rather than concrete implementations, e.g., payment strategies rely on the `PaymentStrategy` interface.
