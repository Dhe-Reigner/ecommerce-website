from django.urls import path
from .views import home, cart, store, checkout
from .import views


urlpatterns = [
    path('', store,name='store'),
    path('cart/', cart,name='cart'),
    path('checkout/', checkout,name='checkout'),
    path('update_item/', views.updateItem,name="update_item")
    
]
