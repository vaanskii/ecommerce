from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('cart/', views.view_cart, name='view_cart'),
    path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('update_cart/<int:item_id>/', views.update_cart, name='update_cart'),
    path('delete_from_cart/<int:item_id>/', views.delete_from_cart, name='delete_from_cart'),
]
