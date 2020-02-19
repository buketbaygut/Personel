from django.http import JsonResponse, response
from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import Personel
from .forms import PersonelForm

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

def delete_personel(request):
    response = dict()
    id = request.GET.get('id')
    personel = Personel.objects.get(pk=id)
    personel.delete()
    response['status'] = True
    return JsonResponse(response, safe=False)

@csrf_exempt
def editPersonel(request):
    response = dict()
    try:
        if request.method == 'GET':
            id = request.GET.get("id")
            personel = Personel.objects.get(id=id)
            response['name'] = personel.name
            response['surname'] = personel.surname
            response['email'] = personel.email
            response['status'] = True
        else:
           id = request.POST.get("id")
           personel = Personel.objects.get(id=id)
           personel.name = request.POST.get("name")
           personel.surname = request.POST.get("surname")
           personel.email = request.POST.get("email")
           personel.save()
           response['status'] = True
    except:
        response['status'] = False
    return JsonResponse(response, safe=False)


def getPersonel(request):
    response = dict()
    personel_list = []
    personel = Personel.objects.all()
    for p in personel:
        temp = dict()
        temp['name'] = p.name
        temp['surname'] = p.surname
        temp['email'] = p.email
        temp['id'] = p.id
        personel_list.append(temp)

    response['personels'] = personel_list
    return JsonResponse(response, safe=False)






