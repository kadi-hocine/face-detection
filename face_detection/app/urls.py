# Fichier urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('searchCustomer',views.searchCustomer, name='search_c'),
    path('listCustomers', views.listCustomers, name='list_c'),
    path('addCustomer', views.addCustomer, name='add_c'),
]
#    path('showCustomer', views.searchCustomer, name='show_c'),