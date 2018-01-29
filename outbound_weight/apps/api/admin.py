from django.contrib import admin

from .models import Calculator


class CalculatorAdmin(admin.ModelAdmin):
    list_display = ['unit_weight', 'longest_side', 'medium_side', 'smallest_side',
                    'size_tier', 'order_date']


admin.site.register(Calculator, CalculatorAdmin)
