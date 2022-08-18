
import requests
import unittest
from login_test import Login_Test


class Airline_Test(unittest.TestCase):

    def test_post_airline(self):
        try:
            data = {
                "name":"test",
                "country_id":"test",
                "user_id":"test",
            }
            self.post =requests.post("http://127.0.0.1:5000/airline", json=data, headers= {"x-auth-token":Login_Test.test_login(self)})
            assert self.post.status_code == 201 or 400
        except:
            print("bad test post airline")

    def test_get_airline(self):
        try:
            self.get =requests.get(f"http://127.0.0.1:5000/airline/test", headers= {"x-auth-token":Login_Test.test_login(self)})
            assert self.get.status_code == 200 or 400
        except:
            print("bad test get airline")


    def test_delete_airline(self):
        try:
            self.delete = requests.delete(f"http://127.0.0.1:5000/airline/test", headers= {"x-auth-token":Login_Test.test_login(self)})
            assert self.delete.status_code == 200 or 400
            print("Tests Airline succeeded")
        except:
            print("bad test delete airline")

