from django.shortcuts import render,redirect
from .models import Personel

#from django.contrib.auth.models import Personel

# Create your views here.
def index(request):

    if request.method == 'POST':
        personels = Personel(
            name = request.POST.get('name'),
            surname = request.POST.get('surname'),
            email = request.POST.get('email'),
            )
        personels.save()
        return redirect('index')
    return render(request,'appKayit/index.html',{})
        
def sil(request):

    personels = Personel.objects.get(id=id)
    personels.delete()
    return redirect('index')

# def duzenle(request):

#     personels = Personel.objects.get(id=id)
#     if request.method=='POST':
#         personels.name = request.POST.get('name')
#         personels.surname = request.POST.get('surname')
#         personels.email = request.POST.get('email')
#         personels.save()
#         return redirect('index')
#     else:
#         return render(request,'appKayit/index.html',{})


        
    

def base(request):
    personels = Personel.objects.all()
    context = {
        'personels': personels
    }

    return render(request,'appKayit/base.html',context)

def duzenle(request):
    if request.method == 'POST':
        personels = Personel(
            name = request.POST.get('name'),
            surname = request.POST.get('surname'),
            email = request.POST.get('email'),
            )
        personels.save()
        return redirect('duzenle')
    return render(request,'appKayit/duzenle.html',{})