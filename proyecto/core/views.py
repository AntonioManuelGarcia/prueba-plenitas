from rest_framework import generics
from core.serializers import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer

# core/views.py
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def get_serializer_context(self):
        return {'request': self.request}

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer
    authentication_classes = []
    permission_classes = []

    def get_serializer_context(self):
        return {'request': self.request}