import json
from django.http import HttpResponse
from django.views.generic.base import View

from outbound_weight.apps.api.api import FBACalculatorAPI
from outbound_weight.apps.api.models import Calculator


class CalculateOutboundData(View):
    """
    Provides request-response interface for 'CalculateFulfillmentFee'
    """

    def get(self, request):
        request_data = dict(
            unit_weight=request.GET.get('unit_weight'),
            medium_side=request.GET.get('medium_side'),
            longest_side=request.GET.get('longest_side'),
            smallest_side=request.GET.get('smallest_side'),
            size_tier=request.GET.get('size_tier'),
            order_date=request.GET.get('order_date')
        )
        if Calculator.objects.filter(**request_data).exists():
            instance = Calculator.objects.get(**request_data)
            return {'weight': instance.weight, 'period': instance.period}
        api = FBACalculatorAPI(**request_data)
        weight = api.get_outbound_shipping_weight()
        period = api.get_calculations_period()
        request_data.update(weight=weight, period=period)
        Calculator.objects.create(**request_data)
        return HttpResponse(json.dumps({'weight': weight, 'period': period}), content='application/json')


class BulkCalculateOutboundData(View):
    """
    Provides request-response interface for 'CalculateFulfillmentFee'
    """

    def get(self, request):
        request_data = dict(
            unit_weight=request.GET.get('unit_weight'),
            medium_side=request.GET.get('medium_side'),
            longest_side=request.GET.get('longest_side'),
            smallest_side=request.GET.get('smallest_side'),
            size_tier=request.GET.get('size_tier'),
            order_date=request.GET.get('order_date')
        )
        if Calculator.objects.filter(**request_data).exists():
            instance = Calculator.objects.get(**request_data)
            return {'weight': instance.weight, 'period': instance.period}
        api = FBACalculatorAPI(**request_data)
        weight = api.get_outbound_shipping_weight()
        period = api.get_calculations_period()
        request_data.update(weight=weight, period=period)
        Calculator.objects.create(**request_data)
        return HttpResponse({'calculations_result': ca}, content='application/json')
