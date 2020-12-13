from rest_framework import serializers
from transacao.models import *

class StatusCompraSerializer(serializers.Serializer):
    code = models.CharField()
    description = models.CharField()

    class Meta:
        fields = (
            'code'
        )

class TotalAmountSerializer(serializers.Serializer):
    amount = models.CharField()
    currency_code = models.CharField()

class CompraSerializer(serializers.Serializer):
    purchase_id = serializers.CharField()
    account_id = serializers.CharField()
    psProductCode = serializers.CharField()
    psProductName = serializers.CharField()
    countryCode = serializers.CharField()
    source = serializers.CharField()
    callingSystemName = serializers.CharField()
    preAuthorization = serializers.BooleanField()
    incrementalAuthorization= serializers.BooleanField()

    class Meta:
        fields = (
            'account_id'
        )



