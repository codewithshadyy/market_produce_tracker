from rest_framework import generics
from django.contrib.auth import get_user_model
User = get_user_model()
from .serializers import RegisterSerializer


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    
