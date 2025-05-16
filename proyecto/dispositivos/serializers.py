from rest_framework import serializers
from .models import Dispositivo

class DispositivoSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Dispositivo
        fields = '__all__'
        read_only_fields = ('created_at',)