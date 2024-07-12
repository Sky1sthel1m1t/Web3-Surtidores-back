from rest_framework import viewsets

from api.models import Combustible
from api.permissions import IsAdministradorSurtidor, IsAdministradorRefineria
from api.serializers.serializers import CombustibleSerializer


class CombustibleViewSet(viewsets.ModelViewSet):
    queryset = Combustible.objects.all()
    serializer_class = CombustibleSerializer
    permission_classes = [
        IsAdministradorSurtidor,
    ]

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [
                IsAdministradorSurtidor,
                IsAdministradorRefineria
            ]
        else:
            permission_classes = [IsAdministradorSurtidor]
        return [permission() for permission in permission_classes]

