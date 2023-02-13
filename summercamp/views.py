from django.shortcuts import render, get_object_or_404
from .models import Camp
from shopping_cart.forms import CartAddProductForm
# Create your views here.

def index(request):
    summercamp = Camp.objects.filter(available = True)
    context = {'summercamp':summercamp}
    return render(request,'summercamp/summercamp.html',context)

def camp_detail(request, id, slug):
    camp = get_object_or_404(Camp, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'summercamp/camp_detail.html',{'camp':camp,'cart_product_form':cart_product_form})