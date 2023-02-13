from django.shortcuts import render, redirect, get_object_or_404
from summercamp.models import Camp
from lessons.models import Lesson
from activities.models import Activity
from django.views.decorators.http import require_POST
from .cart import Cart
from .forms import CartAddProductForm

# Create your views here.
@require_POST
def cart_add(request,camp_id):
    shopping_cart = Cart(request)
    camp = get_object_or_404(Camp,id=camp_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        shopping_cart.add(camp=camp,quantity=cd['quantity'],override_quantity=cd['override'])
    return redirect ('shopping_cart:cart_detail')  

@require_POST
def cart_add(request,lesson_id):
    shopping_cart = Cart(request)
    lesson = get_object_or_404(Lesson,id=lesson_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        shopping_cart.add(lesson=lesson,quantity=cd['quantity'],override_quantity=cd['override'])
    return redirect ('shopping_cart:cart_detail')  

@require_POST
def cart_add(request,activity_id):
    shopping_cart = Cart(request)
    activity = get_object_or_404(Activity,id=activity_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        shopping_cart.add(activity=activity,quantity=cd['quantity'],override_quantity=cd['override'])
    return redirect ('shopping_cart:cart_detail')  

def cart_remove(request, camp_id):
    shopping_cart = Cart(request)
    camp = get_object_or_404(Camp, id=camp_id)
    shopping_cart.remove(camp)  
    return redirect('shopping_cart:cart_detail')

def cart_remove(request, lesson_id):
    shopping_cart = Cart(request)
    lesson = get_object_or_404(Lesson, id=lesson_id)
    shopping_cart.remove(lesson)  
    return redirect('shopping_cart:cart_detail')

def cart_remove(request, activity_id):
    shopping_cart = Cart(request)
    activity = get_object_or_404(Activity, id=activity_id)
    shopping_cart.remove(activity)  
    return redirect('shopping_cart:cart_detail')

def cart_detail(request):
    shopping_cart = Cart(request)
    for item in shopping_cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity':item['quantity'],'override':True})
    return render(request, 'shopping_cart/cart_detail.html',{'shopping_cart':shopping_cart})