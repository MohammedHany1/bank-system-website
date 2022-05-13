from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view customers', views.viewCustomers, name='viewCustomers'),
    path('<int:id>/', views.transfer, name='transfer'),
    path('transfer history', views.trasferHistory, name='transferHistory'),
    path('create customer', views.createCustomer, name='createCustomer'),
]