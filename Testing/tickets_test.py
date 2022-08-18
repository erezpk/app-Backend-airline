
import requests
import unittest
from login_test import Login_Test

class Tickets_Test(unittest.TestCase):

    def test_post_ticket(self):
        try:        
            data = {
                "flight_id":1,
                "customer_id":1,
            }
            self.post =requests.post("http://127.0.0.1:5000/ticket", json=data,headers= {"x-auth-token":Login_Test.test_login(self)})
            assert self.post.status_code == 201
            return self.post.json()

        except:
            print("bad test post ticket")

    def test_get_ticket(self):
        try:
            id = self.test_post_ticket()['ticket']['id']
            self.get =requests.get(f"http://127.0.0.1:5000/ticket/{id}",headers= {"x-auth-token":Login_Test.test_login(self)})
            assert self.get.status_code == 200
        except:
            print("bad test get ticket")

    def test_delete_ticket(self):
        try:
            id = self.test_post_ticket()['ticket']['id']
            self.delete = requests.delete(f"http://127.0.0.1:5000/ticket/{id}",headers= {"x-auth-token":Login_Test.test_login(self)})
            assert self.delete.status_code == 200
            print("Tests Tickets succeeded")
        except:
            print("bad test delete ticket")

