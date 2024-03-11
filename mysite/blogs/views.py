from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Index(request):
    # return HttpResponse("<h1>Hello Django Framework</h1>")
    return render(request,"frontend/index.html")