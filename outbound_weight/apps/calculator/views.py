from django.shortcuts import render
from django.views.generic.base import View

from outbound_weight.apps.calculator.api import FBACalculatorAPI


class FulfillmentFeeAPIView(View):
    """
    Provides request-response interface for 'CalculateFulfillmentFee'
    """
    template_name = 'FulfillmentFeeCalculator.html'

    def get(self, request):
        if not request.GET:
            return render(request, self.template_name, {'form': FulfillmentFeeForm()})
        form = FulfillmentFeeForm(request.GET)
        if form.is_valid():
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