import unittest
from src.customer import Customer
from src.pub import Pub

class TestCustomer(unittest.TestCase):

        def setUp(self): 
            self.customer1 = Customer("Bob",567)
            self.customer2 = Customer("Merlin",85)
            self.customer3 = Customer("Sammy-Jo",420)

        def test_customer_name(self):
            self.assertEqual("Bob", self.customer1.name)

        def test_customer_buys_drink(self):
             self.customer1.buy_drink(3.25)
             self.assertEqual(563.75, self.customer1.wallet)
