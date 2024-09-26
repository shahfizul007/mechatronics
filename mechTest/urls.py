from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    #path('get_pending_orders/', get_pending_orders, name='get_pending_orders'),
    path('im_user/', im_user, name='im_user'),
    path('im_owner/', im_owner, name='im_owner'),
    path('index/', get_product, name='index'),  # Define a URL pattern with the name 'index'
    #path('owner/', owner, name='owner'),
    path('confirm-order/', confirm_order, name='confirm_order'),
    path('owner/', get_pending_orders, name='owner'),  # URL to fetch and display pending orders
    path('orders/received/<int:order_id>/', mark_order_received, name='mark_order_received'),  # URL to mark an order as received
]

