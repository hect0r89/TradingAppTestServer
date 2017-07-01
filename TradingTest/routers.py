from rest_framework.routers import DefaultRouter

from trades.views import TradeViewSet

router = DefaultRouter()

#Assign the view and register the route
router.register(r'trades', TradeViewSet, 'trades-list')