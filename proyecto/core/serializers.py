""" from rest_framework import serializers
from core.models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

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
        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        # Custom claims
        token['user_email'] = user.email
        token['is_active'] = user.is_active
        
        return token """

# core/serializers.py
from rest_framework import serializers
from core.models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .utils import get_client_ip
from dispositivos.models import Dispositivo

class UserSerializer(serializers.ModelSerializer):
    device_name = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'device_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        device_name = validated_data.pop('device_name')
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        
        Dispositivo.objects.create(
            user=user,
            name=device_name,
            ip=get_client_ip(self.context['request']),
            is_active=True
        )
        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    device_name = serializers.CharField(write_only=True, required=True)
    email = serializers.CharField()

    def validate(self, attrs):
        attrs['username'] = attrs.get('email')
        data = super().validate(attrs)
        
        Dispositivo.objects.create(
            user=self.user,
            name=attrs['device_name'],
            ip=get_client_ip(self.context['request']),
            is_active=True
        )
        
        data.update({
            'email': self.user.email,
            'device_registered': True
        })
        return data