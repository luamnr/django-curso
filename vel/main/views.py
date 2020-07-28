from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from . import forms
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def homepage(request):
    return render(request, 'main/homepage.html')


def register(request):
    form = forms.UserForm(request.POST or None)

    context = {
        'register': form,
    }

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        form.save()
        return homepage(request)

    return render(request, 'main/register.html', context)


def log(request):
    if request.method == 'POST':
        postdata = request.POST.copy()
        username = postdata.get('username')
        password = postdata.get('password')

        user = authenticate(request, username=username, password=password)

        print(type(user))

        if user is not None:
            print('TESTE')
            if user.is_active:
                login(request, user)
                return test(request)
        else:
            print('erro')
            return render(request, 'main/homepage.html')

    return render(request, 'main/login.html', {})


@login_required
def test(request):
    return render(request, 'main/test.html', {})


def lout(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))
