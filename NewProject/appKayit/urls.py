from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name = 'index'),
    path('base',views.base,name = 'base'),
    path('duzenle',views.duzenle,name='duzenle'),
]