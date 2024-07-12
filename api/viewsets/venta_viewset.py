from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from api.models import Venta, TanqueGeneral
from api.permissions import IsAdministradorSurtidor, IsVendedor
from api.serializers.serializers import VentaSerializer


class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
    permission_classes = [
        IsVendedor
    ]

    @action(detail=True, methods=['post'], url_path='anular', permission_classes=[IsAdministradorSurtidor])
    def anular_venta(self, request, pk=None):
        venta = self.get_object()
        venta.anulado = True
        venta.save()
        tanque_general = TanqueGeneral.objects.get(
            surtidor=venta.surtidor,
            combustible=venta.combustible
        )
        tanque_general.cantidad_actual += venta.cantidad
        tanque_general.save()
        return Response({'detail': 'Venta anulada'}, status=status.HTTP_200_OK)