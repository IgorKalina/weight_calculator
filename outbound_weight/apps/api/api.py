from .utils import CalculateFulfillmentFee
from .fbacalculator import get_rate_period


class FBACalculatorAPI:
    """
    Class that provides API methods for calculations
    """
    def __init__(self, unit_weight, medium_side, longest_side,
                 smallest_side, size_tier, order_date=None):

        self.unit_weight = unit_weight
        self.medium_side = medium_side
        self.longest_side = longest_side
        self.smallest_side = smallest_side
        self.size_tier = size_tier
        self.order_date = order_date

        self.fulfillment_fee_calculator = CalculateFulfillmentFee()

    def get_outbound_shipping_weight(self):
        return self.fulfillment_fee_calculator.calculate_outbound_shipping_weight(
            unit_weight=self.unit_weight,
            medium_side=self.medium_side,
            longest_side=self.longest_side,
            smallest_side=self.smallest_side,
            size_tier=self.size_tier,
            order_date=self.order_date
        )

    def get_calculations_period(self):
        if self.order_date:
            return get_rate_period(self.order_date)
