from django.urls import path
from .views import Addlocation, Editlocation, Deletelocation, Addshop, Editshop, Deleteshop, Addsales, Editsales, \
    Deletesales, Finishsales, Outstandingbalances, Collection, fun

urlpatterns = [
    path('location/', Addlocation, name='add-location'),
    path('location/edit/<int:pk>/', Editlocation, name='edit-location'),
    path('location/delete/<int:pk>/', Deletelocation, name='delete-location'),
    path('shop/', Addshop, name='add-shop'),
    path('shop/edit/<int:pk>/', Editshop, name='edit-shop'),
    path('shop/delete/<int:pk>/', Deleteshop, name='delete-shop'),
    path('sales/', Addsales, name='add-sales'),
    path('sales/<int:pk>/', Finishsales, name='finish-sales'),
    path('sales/edit/<int:pk>/', Editsales, name='edit-sales'),
    path('sales/delete/<int:pk>/', Deletesales, name='delete-sales'),
    path('balances/', Outstandingbalances, name='outstanding-balances'),
    path('collections/', Collection, name='collections'),
    path('fun/', fun, name='fun'),
]