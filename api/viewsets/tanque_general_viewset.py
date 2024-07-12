from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.models import TanqueGeneral
from api.permissions import IsAdministradorSurtidor, IsChofer
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

    @action(detail=False, methods=['post'], url_path='cargar',
                permission_classes=[IsChofer]
            )
    def cargar_combustible(self, request):
        surtidor = request.data.get('surtidor')
        litros = request.data.get('litros')
        combustible = request.data.get('combustible')
        precio = request.data.get('precio')
        print(surtidor, combustible)
        tanque = TanqueGeneral.objects.filter(surtidor=surtidor, combustible=combustible).first()
        tanque.cantidad_actual += litros
        tanque.precio = precio
        tanque.save()
        return Response({'detail': 'Combustible cargado'}, status=200)
