from rest_framework import viewsets

from api.models import Combustible
from api.permissions import IsAdministradorSurtidor
from api.serializers.serializers import CombustibleSerializer


class CombustibleViewSet(viewsets.ModelViewSet):
    queryset = Combustible.objects.all()
    serializer_class = CombustibleSerializer
    permission_classes = [
        IsAdministradorSurtidor
    ]

