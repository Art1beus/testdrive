from django.shortcuts import render
from .forms import UserForm, CARS
from django.http import HttpResponse, HttpResponseRedirect

users = [
    {'name': 'Смирнов А.В.',
     'phone': '8(988)345-22-12',
     'email': 'smirnov@gmail.com',
     'car': 'Nissan Murano'},
    {'name': 'Петров А.В.',
     'phone': '8(955)345-22-12',
     'email': 'petrov@gmail.com',
     'car': 'Lada Vesta'},
    {'name': 'Сидоров А.В.',
     'phone': '8(922)345-22-12',
     'email': 'sidorov@gmail.com',
     'car': 'Nissan Murano'}
]

def index(request):
    return render(request, 'index.html', context={'users': users})

def about(request):
    return render(request, 'about.html')

def record(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data['name']
            phone = userform.cleaned_data['phone']
            email = userform.cleaned_data['email']
            car = int(userform.cleaned_data['car'])
            comment = userform.cleaned_data['comment']
            car = list(filter(lambda elem: elem[0] == car, CARS))[0][1]

            users.append({'name': name, 'phone': phone, 'email': email, 'car': car})
            # return render(request, 'index.html', context={'users': users})
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('Invalid data')
    else:
        userform = UserForm()
        return render(request, 'record.html', {'form': userform})