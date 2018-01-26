from django.conf.urls import include, url

from .views import BulkCalculateOutboundData, CalculateOutboundData

urlpatterns = [
    url(r'^calculate/', CalculateOutboundData.as_view(), name='calculate'),
    url(r'^bulk_calculate/$', BulkCalculateOutboundData.as_view(), name='bulk_calculate')
]