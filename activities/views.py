from django.shortcuts import render, get_object_or_404
from .models import Activity
from shopping_cart.forms import CartAddProductForm
# Create your views here.

def index(request):
    activities = Activity.objects.filter(available = True)
    context = {'activities':activities}
    return render(request,'activities/activities.html',context)

def activity_detail(request, id, slug):
    activity = get_object_or_404(Activity, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'activities/activity_detail.html',{'activity':activity,'cart_product_form':cart_product_form})