from django.shortcuts import render,redirect,get_object_or_404
from .models import Personel
from .forms import PersonelForm

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
        
def base(request):
    personel = Personel.objects.all()
    context = {
        'personels': personel
    }

    return render(request,'appKayit/base.html',context)

def personel_detail(request,pk):
    personel = get_object_or_404(Personel, pk=pk)
    return render(request,'appKayit/duzenle.html',{'personel':personel})

def duzenlePost(request):
    personel = get_object_or_404(Personel, pk=request.POST.get('id'))  
    form = PersonelForm(request.POST,instance=personel)
    if form.is_valid():
            personel = form.save(commit=False)
            personel.name = request.POST.get('name')
            personel.surname = request.POST.get('surname')
            personel.email = request.POST.get('email')
            personel.save()
            return render(request,'appKayit/duzenle.html',{'form':form})

    return render(request,'appKayit/duzenle.html',{'form':form})

def duzenle(request,pk):
    personel = get_object_or_404(Personel, pk=pk)
    form = PersonelForm(instance=personel)
    return render(request,'appKayit/duzenle.html',{'form':form})

def sil(request,pk):
    personel = get_object_or_404(Personel, pk=pk)
    form = PersonelForm(instance=personel)
    return render(request,'appKayit/index.html',{'form':form})

def silPost(request,pk):

    personel = Personel.objects.get(pk=pk)
    personel.delete()
    
    return render(request,'appKayit/index.html')
