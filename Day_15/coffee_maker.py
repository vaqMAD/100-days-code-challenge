class CoffeeMaker:
    def __init__(self, water: int = 0, milk: int = 0, coffee: int = 0):
        self.water = water
        self.milk = milk
        self.coffee = coffee

    def refill(self):
        self.water = int(
            input("Please type how many water you will refill. Max= 0,5L"))
        self.milk = int(
            input("Please type how many milk you will refill. Max= 0,5L"))
        self.coffee = int(
            (input("Please type how many coffee you will refill. Max= 0,5KG")))

    def report(self):
        """Prit all of the resources"""
        print(f"There is {self.water}ml of water")
        print(f"there is {self.milk}ml of milk")
        print(f"there is {self.coffee}g of coffee")

    def __repr__(self) -> str:
        self.report()

    def is_resource_sufficient(self, menu: dict):

        if menu.ingredients['water'] > self.water:
            print(
                f"Sorry there is not enought water: requied {menu.ingredients['water']}ml, current quantity {self.water}ml. Please ask for refill.")
            print(
                f"Status of rest resorces : \n water: requied {menu.ingredients['water']}ml, current quantity {self.water}ml \n milk : requied {menu.ingredients['milk']}ml, current quantity {self.milk}ml \n coffe : requied {menu.ingredients['coffee']}ml, current quantity {self.coffee}g")
            return False
        elif menu.ingredients['milk'] > self.milk:
            print(
                f"Sorry there is not enought milk: requied {menu.ingredients['milk']}ml, current quantity {self.milk}ml. Please ask for refill.")
            print(
                f"Status of rest resorces : \n water: requied {menu.ingredients['water']}ml, current quantity {self.water}ml \n milk : requied {menu.ingredients['milk']}ml, current quantity {self.milk}ml \n coffe : requied {menu.ingredients['coffee']}ml, current quantity {self.coffee}g")
            return False
        elif menu.ingredients['coffee'] > self.milk:
            print(
                f"Sorry there is not enought coffee: requied {menu.ingredients['coffee']}ml, current quantity {self.coffee}g. Please ask for refill.")
            print(
                f"Status of rest resorces : \n water: requied {menu.ingredients['water']}ml, current quantity {self.water}ml \n milk : requied {menu.ingredients['milk']}ml, current quantity {self.milk}ml \n coffe : requied {menu.ingredients['coffee']}ml, current quantity {self.coffee}g")
            return False
        else:
            return True

    def make_coffee(self, order: dict):
        self.water -= order.ingredients['water']
        self.milk -= order.ingredients['milk']
        self.coffee -= order.ingredients['coffee']
        print(f"Here is your {order.name} ☕️. Enjoy!")