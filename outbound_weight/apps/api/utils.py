from decimal import Decimal, InvalidOperation
from datetime import datetime

from .constants import (
    DIMENSIONAL_WEIGHT_DIVISOR,
    DIMENSIONAL_WEIGHT_DIVISOR_AFTER_FEB_22,
    SM_STD, LG_STD, SM_OVERSIZE, LG_OVERSIZE, SP_OVERSIZE, MD_OVERSIZE)


class CalculateFulfillmentFee:
    def __init__(self):
        self.length = 0
        self.weight = 0
        self.width = 0  # weight from fee preview
        self.height = 0
        self.size_tier = None
        self.order_date = None
        self.today = datetime.now().date()
        print 'Message from {}'.format(__name__)

    def dimensional_weight(self, length, width, height):
        dimensional_weight_divisor = self.get_weight_divisor_by_date()
        dw = (height * length * width) / dimensional_weight_divisor
        return Decimal(dw).quantize(Decimal('0.01'))

    def get_weight_divisor_by_date(self):
        _date = self.today

        if self.order_date:
            _date = self.order_date

        if _date.year >= 2018 and _date.month >= 2 and _date.day >= 22:
            return DIMENSIONAL_WEIGHT_DIVISOR_AFTER_FEB_22

        return DIMENSIONAL_WEIGHT_DIVISOR

    def normalize_data(self):
        """
        we give the dimensions and weight to the Decimal type
        :return: <type 'dict'>
        """
        dimensional_weight_divisor = self.get_weight_divisor_by_date()
        dimensions_dict = dict(
            length=Decimal(str(self.length)),
            width=Decimal(str(self.width)),
            height=Decimal(str(self.height)))
        try:
            dimensions_dict['weight'] = Decimal(str(self.weight))
        except InvalidOperation, error:
            calculated_weight = (dimensions_dict['height'] *
                                 dimensions_dict['length'] *
                                 dimensions_dict['width']) / dimensional_weight_divisor
            dimensions_dict['weight'] = Decimal(calculated_weight).quantize(Decimal('0.1'))
        return dimensions_dict

    def __set_dimensions(self, weight, length, width, height):
        self.weight, self.length, self.width, self.height = weight, length, width, height

    def __set_order_date(self, order_date):
        if order_date:
            self.order_date = order_date

    def __set_product_size_tier(self, product_size_tier):
        self.size_tier = product_size_tier

    def calculate_outbound_shipping_weight(self, unit_weight, medium_side, longest_side, smallest_side, size_tier, order_date=None):
        # set all the necessary data
        if order_date:
            self.__set_order_date(order_date=order_date)
        self.__set_product_size_tier(product_size_tier=size_tier)
        self.__set_dimensions(weight=unit_weight, length=longest_side,
                              width=smallest_side, height=medium_side)

        normalized_dimensions = self.normalize_data()
        dimensional_weight = self.dimensional_weight(length=normalized_dimensions['length'],
                                                     width=normalized_dimensions['width'],
                                                     height=normalized_dimensions['height'])

        if SM_STD in self.size_tier:
            print self.size_tier
            return round(normalized_dimensions['weight'] + Decimal('0.25'))
        elif SP_OVERSIZE in self.size_tier:
            print self.size_tier
            return round(normalized_dimensions['weight'] + Decimal('1.0'))

        if LG_STD in self.size_tier or LG_OVERSIZE in self.size_tier or SM_OVERSIZE in self.size_tier or MD_OVERSIZE in self.size_tier:
            print self.size_tier
            if normalized_dimensions['weight'] < (dimensional_weight + normalized_dimensions['weight']):
                print 'BIP...'
                return round(dimensional_weight + normalized_dimensions['weight'])
            print 'BOOP...'
            return round(normalized_dimensions['weight'])
