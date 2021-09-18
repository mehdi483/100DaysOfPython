from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def work():
    coffee_machine = CoffeeMaker()
    money_manager = MoneyMachine()
    menu = Menu()

    machine_is_on = True
    while machine_is_on:
        chosen_item = input(f"What would you like? {menu.get_items()}: ").lower()

        if chosen_item == 'report':
            coffee_machine.report()
            money_manager.report()
        elif chosen_item == "off":
            print("Turning off...")
            machine_is_on = False
        else:
            drink = menu.find_drink(chosen_item)
            if drink is not None:
                if coffee_machine.is_resource_sufficient(drink):
                    if money_manager.make_payment(drink.cost):
                        coffee_machine.make_coffee(drink)


work()

