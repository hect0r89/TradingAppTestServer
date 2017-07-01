from rest_framework.mixins import UpdateModelMixin, RetrieveModelMixin, ListModelMixin, CreateModelMixin, \
    DestroyModelMixin
from rest_framework.viewsets import GenericViewSet

from trades.models import Trade
from trades.serializers import TradeSerializer


class TradeViewSet(GenericViewSet, ListModelMixin, CreateModelMixin):
    """
    View that only allow create and list trades. 
    Return the queryset order by date.
    """
    queryset = Trade.objects.all().order_by('-date_booked')
    serializer_class = TradeSerializer
