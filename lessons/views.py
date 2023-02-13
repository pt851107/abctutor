from django.shortcuts import render, get_object_or_404
from .models import Lesson
from shopping_cart.forms import CartAddProductForm
# Create your views here.

def index(request):
    lessons = Lesson.objects.filter(available = True)
    context = {'lessons':lessons}
    return render(request,'lessons/lessons.html',context)

def lesson_detail(request, id, slug):
    lesson = get_object_or_404(Lesson, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'lessons/lesson_detail.html',{'lesson':lesson,'cart_product_form':cart_product_form})