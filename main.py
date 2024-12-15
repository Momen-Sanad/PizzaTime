from inventory_manager import InventoryManager
from pizza import Margherita, Pepperoni
from toppings import Cheese, Olives, Mushrooms
from payment import PayPalPayment, CreditCardPayment

def pizza_creation_process():
    inventory_manager = InventoryManager()
    print("Welcome to the Pizza Restaurant!")

    while True:
        print("\nChoose your base pizza:")
        print("0 => Exit")
        print("1. Margherita ($5.0)")
        print("2. Pepperoni ($6.0)")
        pizza_choice = input("Enter the number of your choice: ")

        if pizza_choice == '0':
            break

        if pizza_choice == '1':
            if not inventory_manager.check_and_decrement("Margherita"):
                print("Margherita is out of stock!")
                continue
            pizza = Margherita()
        elif pizza_choice == '2':
            if not inventory_manager.check_and_decrement("Pepperoni"):
                print("Pepperoni is out of stock!")
                continue
            pizza = Pepperoni()
        else:
            print("Invalid choice!")
            continue

        # Add Toppings
        while True:
            print("\nAvailable toppings:")
            print("1. Cheese ($1.0)")
            print("2. Olives ($0.5)")
            print("3. Mushrooms ($0.7)")
            print("4. Finish order")
            topping_choice = input("Enter the number of your choice: ")

            if topping_choice == "1":
                if not inventory_manager.check_and_decrement("Cheese"):
                    print("Cheese is out of stock!")
                    continue
                pizza = Cheese(pizza)
            elif topping_choice == "2":
                if not inventory_manager.check_and_decrement("Olives"):
                    print("Olives are out of stock!")
                    continue
                pizza = Olives(pizza)
            elif topping_choice == "3":
                if not inventory_manager.check_and_decrement("Mushrooms"):
                    print("Mushrooms are out of stock!")
                    continue
                pizza = Mushrooms(pizza)
            elif topping_choice == "4":
                break
            else:
                print("Invalid topping choice!")

        # Display Final Pizza Details
        print("\nYour order:")
        print(f"Description: {pizza.get_description()}")
        print(f"Total cost: ${pizza.get_cost():.2f}")

        # Payment
        print("\nChoose a payment method:")
        print("1. PayPal")
        print("2. Credit Card")
        payment_choice = input("Enter the number of your choice: ")
        if payment_choice == "1":
            payment_method = PayPalPayment()
        elif payment_choice == "2":
            payment_method = CreditCardPayment()
        else:
            print("Invalid payment method!")
            continue

        payment_method.pay(pizza.get_cost())
        print("Payment successful!")

        # Show Remaining Inventory
        print("\nRemaining Inventory:")
        print(inventory_manager.get_inventory())

if __name__ == "__main__":
    pizza_creation_process()