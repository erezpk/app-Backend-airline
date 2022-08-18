
import requests
import unittest
from login_test import Login_Test


class Customers_Test(unittest.TestCase):

    def test_post_customer(self):
        try:
            data = {
                "first_name":"test",
                "last_name":"test",
                "address":"tes@gamil",
                "phone_no":'test',
                "credit_card_no":'test',
                "user_id":34
            }
            self.post =requests.post("http://127.0.0.1:5000/customer", json=data, headers= {"x-auth-token":Login_Test.test_login(self)})
            assert self.post.status_code == 201 or 400
            return self.post.json()
        except:
            print("bad test post customer")

    def test_get_customer(self):
        try:
            id = self.test_post_customer()['customer']['id']
            self.get =requests.get(f"http://127.0.0.1:5000/customer/{id}", headers= {"x-auth-token":Login_Test.test_login(self)})
            assert self.get.status_code == 200
        except :
            print("bad test get customer")



    def test_delete_customer(self):
        try:
            id = self.test_post_customer()['customer']['id']
            self.delete = requests.delete(f"http://127.0.0.1:5000/customer/{id}", headers= {"x-auth-token":Login_Test.test_login(self)})
            assert self.delete.status_code == 200
            print("Tests Customer succeeded")
        except:
            print("bad test delete customer")

