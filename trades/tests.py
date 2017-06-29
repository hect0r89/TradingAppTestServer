import re
from django.test import TestCase
from rest_framework import status

from trades.models import Trade

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

    def test_create_trade_ok(self):
        """
        Ensure we can create a new trade object.
        """
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

    def test_create_trade_id_format_ok(self):
        """
        Ensure id fulfill the format requested.
        """
        data = {'sell_currency': SELL_CURRENCY_TEST, 'sell_amount': SELL_AMOUNT_TEST, 'buy_currency': BUY_CURRENCY_TEST,
                'buy_amount': BUY_AMOUNT_TEST,
                'rate': RATE_TEST}
        response = self.client.post(URL, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Trade.objects.count(), 3)
        self.assertIsNot(re.match("^TR[A-Z0-9]{7}$", str(response.data.get('id'))), None)

    def test_create_repeated_id_ko(self):
        """
        Ensure we can't create a trade object with an existent id.
        """
        id_repeated = Trade.objects.first().id
        data = {'sell_currency': SELL_CURRENCY_TEST, 'sell_amount': SELL_AMOUNT_TEST,
                'buy_currency': BUY_CURRENCY_TEST,
                'buy_amount': BUY_AMOUNT_TEST, 'rate': RATE_TEST, 'id': id_repeated}
        response = self.client.post(URL, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Trade.objects.count(), 2)

    def test_create_trade_blank_sell_currency_ko(self):
        """
        Ensure we can't create a new trade object without sell currency.
        """
        data = {'sell_currency': '', 'sell_amount': SELL_AMOUNT_TEST, 'buy_currency': BUY_CURRENCY_TEST,
                'buy_amount': BUY_AMOUNT_TEST,
                'rate': RATE_TEST}
        response = self.client.post(URL, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Trade.objects.count(), 2)

    def test_create_trade_blank_sell_amount_ko(self):
        """
        Ensure we can't create a new trade object without sell amount.
        """
        data = {'sell_currency': SELL_CURRENCY_TEST, 'sell_amount': '', 'buy_currency': BUY_CURRENCY_TEST,
                'buy_amount': BUY_AMOUNT_TEST,
                'rate': RATE_TEST}
        response = self.client.post(URL, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Trade.objects.count(), 2)

    def test_create_trade_blank_buy_currency_ko(self):
        """
        Ensure we can't create a new trade object without buy currency.
        """
        data = {'sell_currency': SELL_CURRENCY_TEST, 'sell_amount': SELL_AMOUNT_TEST, 'buy_currency': '',
                'buy_amount': BUY_AMOUNT_TEST,
                'rate': RATE_TEST}
        response = self.client.post(URL, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Trade.objects.count(), 2)

    def test_create_trade_blank_buy_amount_ko(self):
        """
        Ensure we can't create a new trade object without buy amount.
        """
        data = {'sell_currency': SELL_CURRENCY_TEST, 'sell_amount': SELL_AMOUNT_TEST, 'buy_currency': BUY_CURRENCY_TEST,
                'buy_amount': '',
                'rate': RATE_TEST}
        response = self.client.post(URL, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Trade.objects.count(), 2)

    def test_create_trade_blank_rate_ko(self):
        """
        Ensure we can't create a new trade object without rate.
        """
        data = {'sell_currency': SELL_CURRENCY_TEST, 'sell_amount': SELL_AMOUNT_TEST, 'buy_currency': BUY_CURRENCY_TEST,
                'buy_amount': BUY_AMOUNT_TEST,
                'rate': ''}
        response = self.client.post(URL, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Trade.objects.count(), 2)

    def test_list_trades_ok(self):
        """
        Ensure we can list all the trade objects.
        """
        response = self.client.get(URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Trade.objects.count(), 2)




