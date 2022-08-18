import unittest
from user_test import Users_Test
from users_roles_test import Users_Roles_Test
from customer_test import Customers_Test
from airline_test import Airline_Test
from countries_test import Countries_Test
from adminstrator_test import Adminstrator_Test
class Test_All(unittest.TestCase):

    def test_for_all(self):
        Users_Test
        Users_Roles_Test
        Customers_Test
        Airline_Test
        Countries_Test
        Adminstrator_Test