from django.urls import path
import basketapp.views as basketapp

app_name = 'basketapp'

urlpatterns = [
    path('', basketapp.basket, name="basket"),
    path('add/<int:pk>/', basketapp.basket_add, name="add"),
    path('del/<int:pk>/', basketapp.basket_del, name="del"),
    path('edit/<int:pk>/<quantity>/', basketapp.basket_edit, name="edit"),
]
