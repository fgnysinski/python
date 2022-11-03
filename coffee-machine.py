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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def coins():
    print("Please insert coins.")
    q = int(input("How many quarters?: ")) * 0.25
    d = int(input("How many dimes?: ")) * 0.10
    n = int(input("How many nickles?: ")) * 0.05
    p = int(input("How many pennies?: ")) * 0.01
    total = q + d + n + p
    return total


def success(received, cost):
    if received >= cost:
        change = round(received - cost, 2)
        print(f"Change: ${change}")
        global profit
        profit += cost
        return True
    else:
        print("That's not enough money.")
        return False


def sufficient(ingredients):
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def make_coffee(name, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {name}.")


x = True
while x:
    coffee = input("What would you like? espresso/latte/cappuccino: ")
    if coffee == 'report':
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}ml")
    elif coffee == 'off':
        x = False
    else:
        drink = MENU[coffee]
        if sufficient(drink['ingredients']):
            payment = coins()
            if success(payment, drink["cost"]):
                make_coffee(coffee, drink['ingredients'])


