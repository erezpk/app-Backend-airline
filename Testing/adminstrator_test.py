
import requests
import unittest
from login_test import Login_Test


class Adminstrator_Test(unittest.TestCase):

    def test_post_adminstrator(self):
        try:
            data = {
                "first_name":"test",
                "last_name":"test",
                "user_id":3
            }
            self.post =requests.post("http://127.0.0.1:5000/admin", json=data, headers= {"x-auth-token":Login_Test.test_login(self)})
            assert self.post.status_code == 201
        except:
            print("bad test post adminstrator")

    def test_get_adminstrator(self):
        try:
            self.get =requests.get(f"http://127.0.0.1:5000/admin/3", headers= {"x-auth-token":Login_Test.test_login(self)})
            assert self.get.status_code == 200
        except:
            print("bad test get adminstrator")


    def test_delete_adminstrator(self):
        try:
            self.delete = requests.delete(f"http://127.0.0.1:5000/admin/3", headers= {"x-auth-token":Login_Test.test_login(self)})
            assert self.delete.status_code == 200 or 400
            print("Tests Adminstrator succeeded")
        except:
            print("bad test delete adminstrator")

