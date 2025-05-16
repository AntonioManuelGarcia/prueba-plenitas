from rest_framework import generics
from core.serializers import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer
    authentication_classes = []
    permission_classes = []

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer