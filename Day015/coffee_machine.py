MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

COINS = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01
}


def ask_payment():
    print("Please insert coins.")
    paid_amount = 0
    for coin_type in COINS:
        paid_amount += int(input(f"how many {coin_type}?:")) * COINS[coin_type]
    return paid_amount


def check_payment(menu_item, paid_amount):
    item_price = MENU[menu_item]["cost"]
    if item_price > paid_amount:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        if item_price < paid_amount:
            print(f"Here is ${round(paid_amount - item_price, 2)} in change.")
        return True


def check_resources(menu_item, current_resource):
    ingredients = MENU[menu_item]["ingredients"]
    for ingredient in ingredients:
        if ingredients[ingredient] > current_resource[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def consume_resources(menu_item, current_resource):
    ingredients = MENU[menu_item]["ingredients"]
    for ingredient in ingredients:
        current_resource[ingredient] -= ingredients[ingredient]

    return current_resource


def show_report(resources, money):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def work():
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }
    money = 0

    machine_is_on = True
    while machine_is_on:
        chosen_item = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if chosen_item == "report":
            show_report(resources, money)
        elif chosen_item == "off":
            print("Turning off...")
            machine_is_on = False
        elif chosen_item in ["espresso", "latte", "cappuccino"]:
            if check_resources(chosen_item, resources):
                paid_amount = ask_payment()
                if check_payment(chosen_item, paid_amount):
                    resources = consume_resources(chosen_item, resources)
                    money += paid_amount
                    print(f"Here is your {chosen_item} ☕️. Enjoy!")

        else:
            print("Your choice is invalid. Please try again.")


work()
