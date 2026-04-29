from django import forms
from .models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('username',)


class CartForm(forms.Form):
	product = forms.ModelChoiceField(queryset=Product.objects.all())
	quantity = forms.IntegerField()


class OrderForm(forms.Form):
	name = forms.CharField()
	address = forms.CharField()
	email = forms.EmailField()
