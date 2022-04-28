drink = "Available"
food = None

def menu(available):
    if available == drink:
        print(drink)
    else:
        print(food)
menu(drink)
menu(food)