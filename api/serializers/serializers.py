import requests
from rest_framework import serializers

from api.constants import Constants
from api.models import Surtidor, Combustible, Bomba, TanqueGeneral, Venta


class SurtidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Surtidor
        fields = '__all__'


class CombustibleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Combustible
        fields = '__all__'


class BombaSerializer(serializers.ModelSerializer):
    combustibles_ids = serializers.PrimaryKeyRelatedField(
        queryset=Combustible.objects.all(),
        source='combustibles',
        many=True,
        write_only=True
    )
    combustibles = CombustibleSerializer(many=True, read_only=True)
    surtidor = SurtidorSerializer(read_only=True)
    surtidor_id = serializers.PrimaryKeyRelatedField(
        queryset=Surtidor.objects.all(),
        source='surtidor',
        write_only=True
    )

    class Meta:
        model = Bomba
        fields = '__all__'


class TanqueGeneralSerializer(serializers.ModelSerializer):
    combustible = CombustibleSerializer(read_only=True)
    combustible_id = serializers.PrimaryKeyRelatedField(
        queryset=Combustible.objects.all(),
        source='combustible',
        write_only=True
    )
    surtidor = SurtidorSerializer(read_only=True)
    surtidor_id = serializers.PrimaryKeyRelatedField(
        queryset=Surtidor.objects.all(),
        source='surtidor',
        write_only=True
    )

    class Meta:
        model = TanqueGeneral
        fields = '__all__'

    def create(self, validated_data):
        tanque_general = TanqueGeneral.objects.create(
            capacidad=validated_data['capacidad'],
            cantidad_actual=validated_data['cantidad_actual'],
            combustible=validated_data['combustible'],
            surtidor=validated_data['surtidor'],
            precio=validated_data['precio']
        )
        headers = {
            'content-type': 'application/json',
            'Authorization': self.context['request'].headers['Authorization']
        }

        try:
            create_tanque_general = requests.post(
                Constants.REFINERIA_URL + 'solicitudes/',
                headers=headers,
                json={
                    "surtidor": tanque_general.surtidor.id,
                    "combustible": tanque_general.combustible.id,
                }
            )
            create_tanque_general.raise_for_status()
        except requests.exceptions.RequestException as e:
            tanque_general.delete()
            raise e
        return tanque_general


class VentaSerializer(serializers.Serializer):
    combustible = CombustibleSerializer(read_only=True)
    surtidor = SurtidorSerializer(read_only=True)
    bomba = BombaSerializer(read_only=True)
    combustible_id = serializers.PrimaryKeyRelatedField(
        queryset=Combustible.objects.all(),
        source='combustible',
        write_only=True
    )
    surtidor_id = serializers.PrimaryKeyRelatedField(
        queryset=Surtidor.objects.all(),
        source='surtidor',
        write_only=True
    )
    bomba_id = serializers.PrimaryKeyRelatedField(
        queryset=Bomba.objects.all(),
        source='bomba',
        write_only=True
    )

    class Meta:
        model = Venta
        fields = '__all__'
