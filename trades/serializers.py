from rest_framework import serializers

from trades.models import Trade


class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = ['sell_amount', 'sell_currency', 'buy_currency', 'rate', 'date_booked']

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['buy_amount'] = instance.sell_amount * instance.rate
        return ret
