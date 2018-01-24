from django.shortcuts import render
from django.views.generic.base import View

from outbound_weight.apps.calculator.api import FBACalculatorAPI
from outbound_weight.apps.calculator.models import Calculator


class FulfillmentFeeAPIView(View):
    """
    Provides request-response interface for 'CalculateFulfillmentFee'
    """
    template_name = 'FulfillmentFeeCalculator.html'

    def get(self, request):
        # if not request.GET:
        #     return render(request, self.template_name, {'form': FulfillmentFeeForm()})
        # form = FulfillmentFeeForm(request.GET)
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
            return {'weight': weight, 'period': calculations_period})
        # if form.is_valid():
        api = FBACalculatorAPI(
            unit_weight=form.cleaned_data['unit_weight'],
            medium_side=form.cleaned_data['medium_side'],
            longest_side=form.cleaned_data['longest_side'],
            smallest_side=form.cleaned_data['smallest_side'],
            size_tier=form.cleaned_data['size_tier'],
            order_date=form.cleaned_data['order_date']
        )
        weight = api.get_outbound_shipping_weight()
        calculations_period = api.get_calculations_period()
        messages.info(request, {'weight': weight, 'period': calculations_period})
        else:
            messages.error(request, "Error")
        return render(request, self.template_name, {'form': form})