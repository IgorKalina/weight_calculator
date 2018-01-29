from __future__ import unicode_literals

from django.db import models


class Calculator(models.Model):
    unit_weight = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    medium_side = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    longest_side = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    smallest_side = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    size_tier = models.CharField(max_length=25)
    order_date = models.DateField(null=True)

    # result of calculations
    weight = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    period = models.CharField(max_length=25)
