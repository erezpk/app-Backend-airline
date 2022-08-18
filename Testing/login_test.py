
import requests
import unittest

class Login_Test(unittest.TestCase):
    
    def test_login(self):
        self.resp =requests.post("http://127.0.0.1:5000/login", json={"username":"user2","password":"password2"})
        assert self.resp.status_code == 200
        return self.resp.json()['access_token']   