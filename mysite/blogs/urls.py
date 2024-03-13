from django.urls import path
from .views import *


urlpatterns = [
    path('',Index),
    path('blogs/<int:id>',blogDetail,name = "blogDetail")
]