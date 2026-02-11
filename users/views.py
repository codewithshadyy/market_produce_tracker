from rest_framework import generics
from django.contrib.auth import get_user_model
User = get_user_model()
from .serializers import RegisterSerializer, PasswordResetRequestSerializer, NewPasswordSerializer

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
    
        

# pass rset view

class PasswordResetView(generics.GenericAPIView):
    serializer_class = PasswordResetRequestSerializer
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"detail": "Password reset email sent."})
    
    
    
#password reset confrim view    
    
class PasswordResetConfirmView(generics.GenericAPIView):
    serializer_class = NewPasswordSerializer
    
    def post(self, request, uidb64, token):
        serializer = self.get_serializer(
            data={
                'password': request.data.get('password'),
                'uidb64': uidb64,
                'token': token
            }
        )
        serializer.is_valid(raise_exception=True)
        return Response({"detail": "Password reset successful."}  )  