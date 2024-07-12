from rest_framework import viewsets

from api.models import Surtidor
from api.permissions import IsAdministradorAccesos
from api.serializers.serializers import SurtidorSerializer


class SurtidorViewSet(viewsets.ModelViewSet):
    queryset = Surtidor.objects.all()
    serializer_class = SurtidorSerializer
    permission_classes = [
        IsAdministradorAccesos
    ]