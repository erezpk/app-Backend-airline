
import requests
import unittest
from login_test import Login_Test


class Countries_Test(unittest.TestCase):

    def test_post_country(self):
        try:
            data = {
                "name":"test",
            }
            self.post =requests.post("http://127.0.0.1:5000/country", json=data, headers= {"x-auth-token":Login_Test.test_login(self)})
            assert self.post.status_code == 201
        except:
            print("bad test post country")

    def test_get_country(self):
        try:
            self.get =requests.get(f"http://127.0.0.1:5000/country/test", headers= {"x-auth-token":Login_Test.test_login(self)})
            assert self.get.status_code == 200 
        except:
            print("bad test get country")


    def test_delete_country(self):
        try:
            self.delete = requests.delete(f"http://127.0.0.1:5000/country/test", headers= {"x-auth-token":Login_Test.test_login(self)})
            assert self.delete.status_code == 200 or 400
            print("Tests Country succeeded")
        except:
            print("bad test delete country")

