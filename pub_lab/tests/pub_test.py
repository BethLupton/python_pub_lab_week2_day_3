import unittest
from src.pub import Pub
from src.customer import Customer


class TestPub(unittest.TestCase):

    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00,[
            {"name":"Beer", "price": 3.25},
            {"name":"Gin", "price": 5.00},
            {"name":"Vodka", "price": 60.00},
            {"name":"Martini","price": 9.50}
            ])
        
    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_increase_till(self):
        self.pub.increase_till(2.50)
        self.assertEqual(102.50, self.pub.till)

    def remove_drink_from_stock(self):
        self.remove_drink({"name":"Beer", "price": 3.25})
        self.assertEqual(self.stock_level,3)

    def test_drink_has_name(self):
        self.assertEqual("Beer", self.pub.drinks[0]["name"])

    def test_sell_drink_to_customer(self):
        customer1 = Customer("Bob",567)
        self.pub.can_sell_drink_to_customer({"name":"Beer", "price": 3.25},customer1)
        self.assertEqual(customer1.wallet, 563.75)
        self.assertEqual(self.pub.increase_till)
        self.assertEqual(self.pub.stock_level(),3)


