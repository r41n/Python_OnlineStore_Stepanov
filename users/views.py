from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart, Customer, CartItem, OrderItem, Order
from .forms import CartForm, OrderForm
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib.auth import logout
from django.contrib import messages


def home_view(request):
    return render(request, 'home.html')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, id=pk)
    return render(request, 'product_detail.html', {'product': product})


def add_to_cart(request):
    if not request.user.is_authenticated:
        return redirect('login')

    customer = get_object_or_404(Customer, user=request.user)
    cart, created = Cart.objects.get_or_create(customer=customer)

    if request.method == 'POST':
        form = CartForm(request.POST)

        if form.is_valid():
            product = form.cleaned_data['product']
            quantity = form.cleaned_data['quantity']

            cart_item, created = CartItem.objects.get_or_create(
                cart=cart,
                product=product
            )

            if not created:
                cart_item.quantity += quantity
            else:
                cart_item.quantity = quantity

            cart_item.save()

            return redirect('cart')

    else:
        form = CartForm()

    return render(request, 'add_to_cart.html', {'form': form})


def placing_an_order(request):
    if not request.user.is_authenticated:
        return redirect('login')

    customer = request.user.customer
    cart = Cart.objects.get(customer=customer)

    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            # создаём заказ
            order = Order.objects.create(
                customer=customer,
                status='new'
            )

            # переносим товары из корзины
            for item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price
                )

            # очищаем корзину
            cart.items.all().delete()

            return redirect('home')

    else:
        form = OrderForm()

    return render(request, 'checkout.html', {'form': form})


def register(request):
    form = CustomUserCreationForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('login')

    return render(request, 'register.html', {'form': form})


def personal_account(request):
    return render(request, 'personal_account.html')


def logout_view(request):
    logout(request)
    messages.success(request, "Вы вышли из личного кабинета")
    return redirect('login')
