from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework import status




User = get_user_model()

class AuthTests(APITestCase):
    def test_user_registration(self):
        url = "/api/auth/register/"
        data = {
            "email":"clienttest@gmail.com",
            'username':"clinto",
            "allowed_markets": "kisii",
            "password":"client10",
            "role":"client"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)
        user = User.objects.first()
        self.assertEqual(user.email, "clienttest@gmail.com")
        
        self.assertTrue(user.check_password("clinto10"))
        
        
     
        
       
        
    def test_duplicate_emails(self):
        User.objects.create_user(
            email = "clienttest@gmail.com",
             username = "clinto",
            password = "client10"
        )  
        response = self.client.post("api/auth/registration", {
            "email":"clienttest@gmail.com",
            'username':"clinto",
            "password":"client10",
        })  
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
