from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User, Customer, Product, Inventory, Cart, CartItem, Order, OrderItem

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Inventory)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)

