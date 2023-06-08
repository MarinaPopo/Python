from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'authentication/home.html')

@login_required
def usersonly(request):
    return render(request, 'authentication/usersonly.html')

@login_required
def privatecontent(request):
    return render(request, 'authentication/privatecontent.html')


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'authentication/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'authentication/signupuser.html', {'form': UserCreationForm(),
                                                                'error': 'Такое имя пользователя уже существует.'})
        else:
            return render(request, 'authentication/signupuser.html', {'form': UserCreationForm(),
                                                            'error': 'Пароли не совпадают.'})



@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'authentication/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'authentication/loginuser.html', {'form': AuthenticationForm()}, {'error': 'Неверные данные'})
        else:
            login(request, user)
            return redirect('home')




