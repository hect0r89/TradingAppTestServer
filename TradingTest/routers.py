from rest_framework.routers import DefaultRouter

from trades.views import TradeViewSet

router = DefaultRouter()

router.register(r'trades', TradeViewSet, 'trades-list')