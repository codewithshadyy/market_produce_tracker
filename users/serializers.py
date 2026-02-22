

from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()

# password reset request modules
from django.contrib.auth.tokens import  PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from django.core.mail import send_mail
from django.conf import settings





# user registration serialzer

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password', 'allowed_markets', 'role']
        
    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            allowed_markets = validated_data['allowed_markets'],
            role=validated_data.get('role', 'CLIENT')
        )
        return user
            

# password reset serializer
class PasswordResetRequestSerializer(serializers.Serializer):
    
    email = serializers.EmailField()
    
    def validate(self, attrs):  
        email = attrs["email"]
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            
            uidb64 = urlsafe_base64_encode(force_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            reset_link = f"http://localhost:8000/api/auth/password-reset-confirm/{uidb64}/{token}/"
            
            
            send_mail(
                 subject="Password Reset",
                message=f"Reset your password: {reset_link}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email]
            )  
            
        return attrs    
            
                    
# password confirm resset serialzer
class NewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(min_length=8)
    uidb64 = serializers.CharField()
    token = serializers.CharField()
    
    def validate(self, attrs):
        try:
            user_id = smart_str(urlsafe_base64_decode(attrs["uidb64"]))
            user = User.objects.get(id=user_id)
            
            if not PasswordResetTokenGenerator().check_token(user,attrs["token"]):
                raise serializers.ValidationError("invalid token")
            
            
            user.set_password(attrs['password'])
            user.save()

            return user
        except Exception:
            
            raise serializers.ValidationError("Invalid reset link")
    