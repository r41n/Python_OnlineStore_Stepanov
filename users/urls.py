from django.urls import path
from django.contrib.auth import views as auth_views
from .views import product_list, product_detail, add_to_cart, placing_an_order, register, home_view, logout_view, personal_account


urlpatterns = [
    path('', home_view, name='home'),
    path('products/', product_list, name='product_list'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('add_to_cart/', add_to_cart, name='add_to_cart'),
    path('placing_an_order/', placing_an_order, name='placing_an_order'),
    path('register/', register, name='register'),
    path('personal_account/', personal_account, name='personal_account'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
]
