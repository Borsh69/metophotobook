from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from django.http import HttpResponse
from .forms import *
from django.contrib.auth import authenticate, login
import string   
import random 
from django.views.decorators.csrf import csrf_protect



def home(request):
    photo = Photo.objects.filter(isopen=True)
    popul_photo = photo.order_by('-popularity')[:5]
    user = User.objects.all()
    close_photo = Photo.objects.filter(isopen=False)
    form = SignInForm()
    context = {'close_photo': close_photo,'photo_popul': popul_photo, 'user': user, 'form': form}
    return render(request, 'base/home.html', context)

def contest(request):
    return render(request, 'base/contest-details.html')

def albums(request):
    albums = Album.objects.all()

    context = {'albums': albums}
    print(albums.count())
    return render(request, 'base/albums.html', context)


def user(request):
    return render(request, 'base/users.html')

def album(request, pk):
    album = Album.objects.get(id = pk)
    context = {'album': album}
    return render(request, 'base/album.html', context)

def contests(request):
    return render(request, 'base/contests.html')


@csrf_protect
def signin(request):
    if 'id' in request.session:
        id_per = int(request.session['id'])
        user = User.objects.get(id=id_per)
        return redirect('/')
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                usr_account = User.objects.get(email=cd["email"])
            except User.DoesNotExist:
                print("Error")
                return redirect('/')
            if(usr_account.password == cd["password"]):
                id_usr = int(usr_account.id)
                request.session.set_expiry(24*3600)
                request.session['id'] = id_usr
                response = redirect(f'/')
                return response
            else:
                print("Error")

        else:
            print("Error")
    else:
        form = SignInForm()
        print("SENT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    return render(request, 'base/home.html', {'form': form})