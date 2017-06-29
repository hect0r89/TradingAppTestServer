from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse

from trades.models import Trade
from trades.serializers import TradeSerializer

URL = '/api/1.0/trades/'
SELL_CURRENCY_TEST = 'GBP'
SELL_AMOUNT_TEST = 5054.98
BUY_CURRENCY_TEST = 'EUR'
BUY_AMOUNT_TEST = 4778.89
RATE_TEST = 1.2756


class TradeTestCase(TestCase):
    def setUp(self):
        Trade.objects.create(sell_currency='USD', sell_amount=500, buy_currency='EUR', buy_amount=633.13, rate=1.2756)
        Trade.objects.create(sell_currency='GBP', sell_amount=1250.50, buy_currency='USD', buy_amount=1023.89,
                             rate=0.9801)

    def test_trades_post(self):
        data = {'sell_currency': SELL_CURRENCY_TEST, 'sell_amount': SELL_AMOUNT_TEST, 'buy_currency': BUY_CURRENCY_TEST,
                'buy_amount': BUY_AMOUNT_TEST,
                'rate': RATE_TEST}
        response = self.client.post(URL, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Trade.objects.count(), 3)
        self.assertEqual(Trade.objects.filter(pk=response.data.get('id')).first().sell_currency, SELL_CURRENCY_TEST)
        self.assertEqual(Trade.objects.filter(pk=response.data.get('id')).first().sell_amount, SELL_AMOUNT_TEST)
        self.assertEqual(Trade.objects.filter(pk=response.data.get('id')).first().buy_currency, BUY_CURRENCY_TEST)
        self.assertEqual(Trade.objects.filter(pk=response.data.get('id')).first().buy_amount, BUY_AMOUNT_TEST)
        self.assertEqual(Trade.objects.filter(pk=response.data.get('id')).first().rate, RATE_TEST)
