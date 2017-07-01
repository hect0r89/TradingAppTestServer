from rest_framework import serializers

from trades.models import Trade


class TradeSerializer(serializers.ModelSerializer):
    """
    Serializer for Trade model
    """
    class Meta:
        model = Trade
        fields = '__all__'

    def to_representation(self, instance):
        """
        Method that calculate the buy amount and represent in the serializer
        """
        ret = super().to_representation(instance)
        ret['buy_amount'] = instance.sell_amount * instance.rate
        return ret
