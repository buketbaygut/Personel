from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name = 'index'),
    path('base/',views.base,name = 'base'),
    path('delete_personel',views.delete_personel,name='delete_personel'),
    path('base/editPersonel',views.editPersonel,name='editPersonel'),
    path('base/getPersonels',views.getPersonel,name='getPersonels'),
]