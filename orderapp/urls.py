from django.urls import path, include

import orderapp.views as orderapp
from geekshop import settings

app_name = 'orderapp'

urlpatterns = [
    path('', orderapp.OrderList.as_view(), name='orders_list'),
    path('forming/complete/<pk>/', orderapp.order_forming_complete, name='order_forming_complete'),
    path('create/', orderapp.OrderItemsCreate.as_view(), name='order_create'),
    path('read/<pk>/', orderapp.OrderRead.as_view(), name='order_read'),
    path('update/<pk>/', orderapp.OrderItemsUpdate.as_view(), name='order_update'),
    path('delete/<pk>/', orderapp.OrderDelete.as_view(), name='order_delete'),
]