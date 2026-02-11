from rest_framework import generics
from django.contrib.auth import get_user_model
User = get_user_model()
from .serializers import RegisterSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

# user registration view
class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class UserLogOutView(APIView):
    permission_classes = [IsAuthenticated]
        
    def post(self, request):
        try:
            refresh_token = request.dat["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            
            return Response(
                {"message":"logged out successfully"},
                status=status.HTTP_205_RESET_CONTENT
            )
        except Exception:
            return Response(
                {"error":"inavalid token"},
                status=status.HTTP_400_BAD_REQUEST
            )    
    
        
