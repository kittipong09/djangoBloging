from django.shortcuts import render
from django.http import HttpResponse
from category.models import Category

# Create your views here.
def Index(request):
    # return HttpResponse("<h1>Hello Django Framework</h1>")
    categories = Category.objects.all()
    return render(request,"frontend/index.html",{'categories':categories})