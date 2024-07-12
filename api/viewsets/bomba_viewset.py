from rest_framework import viewsets
from rest_framework.response import Response

from api.models import Bomba
from api.permissions import IsAdministradorSurtidor
from api.serializers.serializers import BombaSerializer


class BombaViewSet(viewsets.ModelViewSet):
    queryset = Bomba.objects.all()
    serializer_class = BombaSerializer
    permission_classes = [
        IsAdministradorSurtidor
    ]

    def list(self, request, *args, **kwargs):
        token = request.auth
        surtidor_id = token['surtidor']
        queryset = Bomba.objects.filter(surtidor=surtidor_id)
        serializer = BombaSerializer(queryset, many=True)
        return Response(serializer.data)