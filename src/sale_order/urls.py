from django.urls import path
from .views import (
    SaleOrderListView,
    SaleOrderDetailView,
    SaleOrderCreateView,
    SaleOrderUpdateView,
    SaleOrderDeleteView
)

app_name = "sale_order"

urlpatterns = [
    path('', SaleOrderListView.as_view(), name='order_list'),
    path('create/', SaleOrderCreateView.as_view(), name='order_create'),
    path('<int:id>/', SaleOrderDetailView.as_view(), name='order_detail'),
    path('<int:id>/update/', SaleOrderUpdateView.as_view(), name='order_update'),
    path('<int:id>/delete/', SaleOrderDeleteView.as_view(), name='order_delete'),

]
