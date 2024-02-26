from django.urls import path

from shop.apps import ShopConfig
from shop.views import ItemRetrieveApiView, PaymentRetrieveApiView

app_name = ShopConfig.name

urlpatterns = [
    path('item/<int:pk>/', ItemRetrieveApiView.as_view(), name='item'),
    path('buy/<int:pk>/', PaymentRetrieveApiView.as_view(), name='buy')
]