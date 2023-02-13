from django.shortcuts import render, get_object_or_404
from .models import Daycare
from shopping_cart.forms import CartAddProductForm

# Create your views here.


def index(request):
    daycare = Daycare.objects.filter(available=True)
    context = {'daycare': daycare}
    return render(request, 'daycare/daycare.html', context)


def daycare_detail(request, id, slug):
    daycare = get_object_or_404(Daycare, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'daycare/daycare_detail.html', {'daycare': daycare, 'cart_product_form': cart_product_form})
