

import requests
import unittest
from login_test import Login_Test

class Users_Roles_Test(unittest.TestCase):
    
    def test_get_all_users_roles(self):
        self.get =requests.get(f"http://127.0.0.1:5000/all_users_roles", headers= {"x-auth-token":Login_Test.test_login(self)})
        assert self.get.status_code == 200
        print("Tests users roles succeeded")


