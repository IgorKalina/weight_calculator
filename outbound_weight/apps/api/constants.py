from decimal import Decimal

PICK_PACK = {
    "Standard": Decimal("1.06"),
    "SML_OVER": Decimal("4.09"),
    "MED_OVER": Decimal("5.20"),
    "LRG_OVER": Decimal("8.40"),
    "SPL_OVER": Decimal("10.53"),
}

THIRTY_DAY = {
    "Standard": Decimal('0.5525'),
    "Oversize": Decimal('0.4325'),
}

DIMENSIONAL_WEIGHT_DIVISOR = Decimal('166.0')
CUBIC_FOOT_DIVISOR = Decimal('1728.0')

FEE_WEIGHT = 12.0/16.0
FEE_WEIGHT_MEDIA = 14.0/16.0

CLOSING_FEES = {
    'referral': Decimal('0.15'),
    'media': Decimal('1.35'),
    'apparel': Decimal('0.40'),
    'non-pro': Decimal('1.0'),
}

SM_STD = 'Sm-Std'
LG_STD = 'Lg-Std'
SM_OVERSIZE = 'Sm-Oversize'
MD_OVERSIZE = 'Md-Oversize'
LG_OVERSIZE = 'Lg-Oversize'
SP_OVERSIZE = 'Sp-Oversize'

SPECIAL_OVERSIZE = 'SPECIAL_OVERSIZE'
OVERSIZE = 'OV'
STANDARD = 'ST'
NO_WEIGHT = 'NO_WEIGHT'
NO_AMAZON_ESTIMATED_FEE = 'NO_AMAZON_ESTIMATED_FEE'
WRONG_TYPES = ['--', '', None]
ORDER_FEE = 'order_fee'
UNIT_FEE = 'unit_fee'
WEIGHT_FEE = 'weight_fee'
PER_UNIT_FEE = 'per-unit fee'
JANUARY_SEPTEMBER = [1, 2, 3, 4, 5, 6, 7, 8, 9]
JANUARY_OCTOBER = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
OCTOBER_DECEMBER = [10, 11, 12]
NOVEMBER_DECEMBER = [11, 12]
DIMENSIONAL_WEIGHT_DIVISOR_AFTER_FEB_22 = Decimal('139.0')

PACKAGING_WEIGHT = (
    ('Small-std-size', Decimal('0.25')),  # Unit weight + packaging weight (total rounded up to the nearest whole pound)
    ('Large-std-size', Decimal('0.25')),  #  The greater of the unit weight or dimensional weight + packaging weight (total rounded up to the nearest whole pound)
    ('Oversize-media-and-non-media', Decimal('1.0')),  #  The greater of the unit weight or dimensional weight + packaging weight (total rounded up to the nearest whole pound)
    ('Special-oversize', Decimal('1.0'))  # Unit weight + packaging weight (total rounded up to the nearest whole pound)
)

ORDER_DATE_FMT = '%Y-%m-%d'
