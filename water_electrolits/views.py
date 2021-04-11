from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from water_electrolits.models import General_Information, Person, Human
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import requests
import json
import csv


def page(request):
    return HttpResponse('It is main page!')


def names(request):
    ls = []
    for x in General_Information.objects.all():
        ls.append(x.diagnosis)
    a = ' '.join(ls)
    return HttpResponse(a)


def home_page(request):
    context = {}
    return render(request, 'index.html', context)


def onco_main(request):
    context = {}
    return render(request, 'gr_project.html', context)


def enter_page(request):
    context = {}
    return render(request, 'enter_page.html', context)


def error(request):
    context = {}
    return render(request, 'error.html', context)


def log(request):
    context = {}
    return render(request, 'logout.html', context)


def login_user(request):
    user = authenticate(
        username=request.POST['user'],
        password=request.POST['unknown']
    )
    if user is None:
        return render(request, 'error.html')
    else:
        login(request, user)
        return HttpResponseRedirect('onco')



def do_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('onco')
    else:
        return HttpResponseRedirect('out')


def register(request):
    user = User.objects.create_user(
        request.POST['login'],
        password=request.POST['password'],
        email='mail@a.b'
    )

    return HttpResponseRedirect('onco')


def show_registration(request):
    context = {}
    return render(request, 'reg_form.html', context)

def zadachi(request):
    context = {}
    return render(request, 'zadachi.html', context)

def obmen(request):
    response={
        'num': request.POST['n']
    }
    return JsonResponse(response)

def uniq(request):
    users=User.objects.filter(username=request.POST['login'])
    if len(users)!=0:
        response={
            'exist': 1
        }
    else:
        response={
            'exist': 0
        }

    return JsonResponse(response)

def test(request):
    if request.user.has_perm('water_electrolits.view_analizes'):
        print("Посмотри на анализы, ты здоров")
    else:
        print("Низя смотреть на анализы.")

    return render(request, 'gr_project.html',)

def currency(request):
    response = requests.get(' https://www.nbrb.by/api/exrates/rates/dynamics/145?startdate=2021-1-31&enddate=2021-2-6')
    data = json.loads(response.text)
    sum = 0
    for x in data:
        sum+=x['Cur_OfficialRate']
    average = sum/7
    print(average)
    return HttpResponse(average)

def photo(request):
    context ={'ph1': Person.objects.filter(id=1)[0],
              'ph2': Person.objects.filter(id=2)[0],
              'ph3': Person.objects.filter(id=3)[0]}
    return render(request, 'gr_project.html', context)

def server(request):
    if len(request.POST['name']) > 3:
        Human.objects.filter(
            id=request.POST['id']
        ).update(
            name = str(request.POST['name']),
            age = int(request.POST['age'])
        )
        return JsonResponse({'status': 'OK'})
    else:
        return JsonResponse({'status': 'Error'})

def get_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = \
        'attachment; filename=table.csv'

    writer = csv.writer(response)
    writer.writerow(['age', 'name'])
    persons = Human.objects.all()
    for person in persons:
        writer.writerow([person.age, person.name])
    return response




