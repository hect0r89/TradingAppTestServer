import random
import string

from django.db import models


def generate_id():
    return 'TR' + ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))


class Trade(models.Model):
    """Trade model"""
    id = models.CharField('id', primary_key=True, blank=False, null=False, unique=True, default=generate_id, max_length=9)
    sell_currency = models.CharField('Sell currency', blank=False, null=False, max_length=3)
    sell_amount = models.FloatField('Sell amount', blank=False, null=False)
    buy_currency = models.CharField('Buy currency', blank=False, null=False, max_length=3)
    buy_amount = models.FloatField('Buy amount', blank=False, null=False)
    rate = models.FloatField('Rate', blank=False, null=False)
    date_booked = models.DateTimeField('Date booked', blank=False, null=False, auto_now=True)

