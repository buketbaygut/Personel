from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name = 'index'),
    path('base',views.base,name = 'base'),
    path('appKayit/<int:pk>/',views.personel_detail,name='personel_detail'),
    path('appKayit/<int:pk>/duzenle/',views.duzenle,name='duzenle'),
    path('appKayit/<int:pk>/sil',views.sil,name='sil'),
    path('appKayit/duzenle/',views.duzenlePost,name='duzenlePost'),
    path('appKayit/sil/',views.silPost,name='silPost')

]