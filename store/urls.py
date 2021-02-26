from django.urls import path
from allauth.account.views import LoginView, LogoutView, SignupView
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('checkout', views.checkout, name='checkout'),
    path('products', views.products, name='products'),
    path('cart', views.cart, name='cart'),
    path('add_to_cart/<int:pk>', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:pk>', views.remove_from_cart, name='remove_from_cart'),
    path('decrease_amount_of_item/<int:pk>', views.decrease_amount_of_item, name='decrease_amount_of_item'),
    path('accounts/login', LoginView.as_view(), name='login'),
    path('accounts/logout', LogoutView.as_view(), name='logout'),
    path('accounts/signup', SignupView.as_view(), name='signup'),
]
