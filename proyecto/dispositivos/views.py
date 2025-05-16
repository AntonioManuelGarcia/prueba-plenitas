from rest_framework import viewsets
from .models import Dispositivo
from .serializers import DispositivoSerializer
from rest_framework.permissions import IsAuthenticated

class DispositivoViewSet(viewsets.ModelViewSet):
    serializer_class = DispositivoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Dispositivo.objects.filter(user=self.request.user)