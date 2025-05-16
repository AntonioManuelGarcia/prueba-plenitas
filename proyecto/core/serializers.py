# core/serializers.py
from rest_framework import serializers
from core.models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .utils import get_client_ip, get_client_device
from dispositivos.models import Dispositivo

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        
        Dispositivo.objects.create(
            user=user,
            name=get_client_device(self.context['request']),
            ip=get_client_ip(self.context['request']),
            is_active=True
        )
        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    email = serializers.CharField()

    def validate(self, attrs):
        attrs['username'] = attrs.get('email')
        data = super().validate(attrs)
        
        Dispositivo.objects.create(
            user=self.user,
            name=get_client_device(self.context['request']),
            ip=get_client_ip(self.context['request']),
            is_active=True
        )
        
        data.update({
            'email': self.user.email,
            'device_registered': True
        })
        return data