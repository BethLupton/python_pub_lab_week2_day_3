class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks

    def increase_till(self, amount):
        self.till += amount

    def stock_level(self, drinks):
        return len(self.drinks)
    
    def remove_drink(self,drink):
        self.drinks.remove(drink)

    # def can_sell_drink_to_customer(self, drinks, customer):
        
