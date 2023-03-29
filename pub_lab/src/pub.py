class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks

    def increase_till(self, amount):
        self.till += amount

    def stock_level(self):
        return len(self.drinks)
    
    def remove_drink(self,drink):
        self.drinks.remove(drink)

    # def can_sell_drink_to_customer(self, drink, customer):
    #     drink_to_sell = self.drinks(drink)
    #     customer.buy_drink(drink_to_sell["price"])
    #     self.increase_till(drink_to_sell["price"])
    #     self.remove_drink(drink_to_sell)
