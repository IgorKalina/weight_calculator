from __future__ import unicode_literals

from django.db import models


class Calculator(models.Model):
    unit_weight = models.IntegerField()
    medium_side = models.IntegerField()
    longest_side = models.IntegerField()
    smallest_side = models.IntegerField()
    size_tier = models.CharField(max_length=16)
    order_date = models.DateField(null=True)

    # result of calculations
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    period = models.CharField(max_length=16)
