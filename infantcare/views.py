from django.shortcuts import render, get_object_or_404
from .models import Infantcare
from shopping_cart.forms import CartAddProductForm
# Create your views here.


def index(request):
    infantcare = Infantcare.objects.filter(available=True)
    context = {'infantcare': infantcare}
    return render(request, 'infantcare/infantcare.html', context)


def infantcare_detail(request, id, slug):
    infantcare_case = get_object_or_404(
        Infantcare, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'infantcare/infantcare_detail.html', {'infantcare_case': infantcare_case, 'cart_product_form': cart_product_form})
