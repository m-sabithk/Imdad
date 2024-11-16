from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .models import *
# Create your views here.


@login_required(login_url='/signin')
def home(request):

    user = request.user

    profile = Profile.objects.get(user = user)
    expence = Expence.objects.all()
    Given_expence = GivenExpence.objects.filter(student = profile)
    # pendign = Expence.objects.filter(student = profile, expence = Given_expence.expence)

    context = {'host': profile,'expences': expence, 'Given_expences': Given_expence}
    return render(request, 'index.html', context)


# def signup(request):

#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         contact = request.POST.get('contact')
#         password = request.POST.get('password')
#         password2 = request.POST.get('password2')
        
#         if User.objects.filter(username=username).exists():
#             raise ValueError("This username already exists")
#         else:
#             if password == password2:
#                 user = User.objects.create(username=username, password=password, email = email)
#                 user.save()
#                 profile = Profile.objects.create(user=user, contact_no = contact)
#                 profile.save()

#                 login(request, user)
#                 return redirect('home')
#     context = {}
#     return render(request, 'signup.html', context)

def signin(request):
    if request.method == 'POST':
        if request.POST.get('signin'):
            username = request.POST.get('username')
            password = request.POST.get('password')

            try:
                User.objects.get(username=username)
            except:
                return HttpResponse(f'There is not an account with username {username}')

            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return HttpResponse('Username or Password is incorrect')
            
        elif request.POST.get('signup'):
            username = request.POST.get('username')
            email = request.POST.get('email')
            contact = request.POST.get('contact')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')
            
            if User.objects.filter(username=username).exists():
                raise ValueError("This username already exists")
            else:
                if password == password2:
                    user = User.objects.create(username=username, password=password, email = email)
                    user.save()
                    profile = Profile.objects.create(user=user, contact_no = contact)
                    profile.save()

                    login(request, user)
                    return redirect('home')

        
    context = {}
    return render(request, 'signin.html', context)

def signout(request):
    logout(request)
    return redirect('home')
