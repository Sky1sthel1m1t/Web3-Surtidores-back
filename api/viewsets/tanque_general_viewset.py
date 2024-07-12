from rest_framework import viewsets
from rest_framework.response import Response

from api.models import TanqueGeneral
from api.permissions import IsAdministradorSurtidor
from api.serializers.serializers import TanqueGeneralSerializer


class TanqueGeneralViewSet(viewsets.ModelViewSet):
    queryset = TanqueGeneral.objects.all()
    serializer_class = TanqueGeneralSerializer
    permission_classes = [
        IsAdministradorSurtidor
    ]

    def list(self, request, *args, **kwargs):
        token = request.auth
        surtidor_id = token['surtidor']
        queryset = TanqueGeneral.objects.filter(surtidor=surtidor_id)
        serializer = TanqueGeneralSerializer(queryset, many=True)
        return Response(serializer.data)

