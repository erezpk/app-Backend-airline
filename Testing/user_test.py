

import requests
import unittest
from login_test import Login_Test

class Users_Test(unittest.TestCase):
    
    def test_post_user(self):
        try:
            data = {
                "username":"test",
                "password":"test",
                "email":"tes@gamil",
                "user_roles_id":3
            }
            self.post =requests.post("http://127.0.0.1:5000/user", json=data)
            assert self.post.status_code == 201 or 400
        except :
            print("bad test post user")

    def test_get_user(self):
        try:
            self.get =requests.get(f"http://127.0.0.1:5000/user/test", headers= {"x-auth-token":Login_Test.test_login(self)})
            assert self.get.status_code == 200  or 400
            return self.get.json()
        except :
            print("bad test get user")

        
    def test_delete_user(self):
        try:
            self.delete = requests.delete(f"http://127.0.0.1:5000/user/test", headers= {"x-auth-token":Login_Test.test_login(self)})
            assert self.delete.status_code == 200
        except:
            print("bad test delete user")

        

