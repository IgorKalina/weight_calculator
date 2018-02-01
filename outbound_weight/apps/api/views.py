import json
from django.http import HttpResponse, JsonResponse
from django.views.generic.base import View
from datetime import datetime

from outbound_weight.apps.api.api import FBACalculatorAPI
from outbound_weight.apps.api.models import Calculator

from .constants import ORDER_DATE_FMT
from .utils import parse_str_to_list


class CalculateOutboundData(View):
    """
    Provides request-response interface for 'CalculateFulfillmentFee'
    """

    def get(self, request):
        if Calculator.objects.filter(**request.GET.dict()).exists():
            instance = Calculator.objects.get(**request.GET.dict())
            return JsonResponse({'asin': instance.asin, 'weight': str(instance.weight), 'period': instance.period},
                                content_type='application/json')
        request_data = dict(
            unit_weight=request.GET.get('unit_weight'),
            medium_side=request.GET.get('medium_side'),
            longest_side=request.GET.get('longest_side'),
            smallest_side=request.GET.get('smallest_side'),
            size_tier=request.GET.get('size_tier'),
            order_date=datetime.strptime(request.GET.get('order_date'), ORDER_DATE_FMT)
        )
        api = FBACalculatorAPI(**request_data)
        weight = api.get_outbound_shipping_weight()
        period = api.get_calculations_period()
        request_data.update(weight=weight, period=period)
        Calculator.objects.update_or_create(asin=request.GET.get('asin'), defaults=request_data)
        return JsonResponse({'asin': request.GET.get('asin'), 'weight': weight, 'period': period},
                            content_type='application/json')


class BulkCalculateOutboundData(View):
    """
    Provides request-response interface for 'CalculateFulfillmentFee'
    """

    def get(self, request):
        request_data = dict()
        calculation_result = dict()

        if request.GET.get('list_of_items'):
            list_of_items = parse_str_to_list(request.GET.get('list_of_items'))
            for item in list_of_items:
                item = {k: str(v) for k, v in item.items()}
                if Calculator.objects.filter(**item).exists():
                    instance = Calculator.objects.get(**item)
                    calculation_result[instance.asin] = dict(weight=str(instance.weight),
                                                             period=instance.period)
                request_data[item['asin']] = dict(
                    unit_weight=item.get('unit_weight'),
                    longest_side=item.get('longest_side'),
                    medium_side=item.get('medium_side'),
                    smallest_side=item.get('smallest_side'),
                    size_tier=item.get('size_tier'),
                    order_date=datetime.strptime(item.get('order_date'), ORDER_DATE_FMT)
                )
        if request_data:
            for asin, item in request_data.items():
                api = FBACalculatorAPI(**item)
                calculation_result[asin] = dict(
                    weight=str(api.get_outbound_shipping_weight()),
                    period=api.get_calculations_period()
                )
                item.update(calculation_result.get(asin))
                Calculator.objects.update_or_create(asin=asin, defaults=item)

        if calculation_result:
            return JsonResponse({'calculations_result': calculation_result}, content_type='application/json')

        return JsonResponse({'calculation_result': 'No_result'}, content_type='application/json')
