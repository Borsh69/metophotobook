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
    owner = None
    if 'id' in request.session:
        id_per = int(request.session['id'])
        p = True
        owner = User.objects.get(id=id_per)
    else:
        owner = User.objects.get(username="test")
        p = False

    photo = Photo.objects.filter(isopen=True)
    popul_photo = photo.order_by('-popularity')[:5]
    user = User.objects.all()
    close_photo = Photo.objects.filter(isopen=False)
    INform = SignInForm()
    form = SignUpForm()
    context = { 'close_photo': close_photo,
                'photo_popul': popul_photo,
                'user': user,
                'INform': INform,
                'form' : form,
                'owner':owner,
                "p": p
            }
    return render(request, 'base/home.html', context)

def contest(request):
    owner = None
    if 'id' in request.session:
        p = True
        id_per = int(request.session['id'])
        owner = User.objects.get(id=id_per)
    else:
        p = False
        owner = User.objects.get(username="test")
    INform = SignInForm()
    form = SignUpForm()
    photo = Photo.objects.filter(isopen=True)
    user = User.objects.all()
    close_photo = Photo.objects.filter(isopen=False)
    context = { 'close_photo': close_photo,
                'user': user,
                'owner':owner,
                'INform': INform,
                'form' : form,
                "photo" : photo,
                "p": p
            }
    return render(request, 'base/contest-details.html', context)

def albums(request):
    owner = None
    if 'id' in request.session:
        p = True
        id_per = int(request.session['id'])
        owner = User.objects.get(id=id_per)
    else:
        p = False
        owner = User.objects.get(username="test")
    albums = Album.objects.all()
    INform = SignInForm()
    form = SignUpForm()
    photo = Photo.objects.filter(isopen=True)
    user = User.objects.all()
    close_photo = Photo.objects.filter(isopen=False)
    context = { 'close_photo': close_photo,
                'user': user,
                'owner':owner,
                'INform': INform,
                'form' : form,
                "photo" : photo,
                'albums': albums,
                "p": p
            }
    return render(request, 'base/albums.html', context)


def user(request):
    owner = None
    if 'id' in request.session:
        p = True
        id_per = int(request.session['id'])
        owner = User.objects.get(id=id_per)
    else:
        p = False
        owner = User.objects.get(username="test")
        return redirect('/')
    albums = Album.objects.all()    
    form = AlbumForm()

    photo = Photo.objects.filter(isopen=True)
    user = User.objects.all()
    close_photo = Photo.objects.filter(isopen=False)
    context = { 'close_photo': close_photo,
                'user': user,
                'owner':owner,
                'form' : form,
                "photo" : photo,
                'albums': albums,
                "p": p
            }
    return render(request, 'base/users.html', context)

def album(request, pk):
    owner = None
    if 'id' in request.session:
        p = True
        id_per = int(request.session['id'])
        owner = User.objects.get(id=id_per)
    else:
        p = False
        owner = User.objects.get(username="test")
    albums = Album.objects.get(id = pk)
    photo = Photo.objects.filter(isopen=True)
    user = User.objects.all()
    INform = SignInForm()
    form = PhotoForm()
    close_photo = Photo.objects.filter(isopen=False)
    context = { 'close_photo': close_photo,
                'user': user,
                'INform': INform,
                'form' : form,
                'owner':owner,
                "photo" : photo,
                'albums': albums,
                "p": p,
                "pk":pk,
            }
    
    return render(request, 'base/album.html', context)

def photoes(request):
    owner = None
    if 'id' in request.session:
        p = True
        id_per = int(request.session['id'])
        owner = User.objects.get(id=id_per)
    else:
        p = False
        owner = User.objects.get(username="test")
    albums = Album.objects.all()
    INform = SignInForm()
    form = SignUpForm()
    photo = Photo.objects.filter(isopen=True)
    user = User.objects.all()
    close_photo = Photo.objects.filter(isopen=False)
    context = { 'close_photo': close_photo,
                'user': user,
                'owner':owner,
                'INform': INform,
                'form' : form,
                "photo" : photo,
                'albums': albums, 
                "p": p
            }
    return render(request, 'base/photoes.html', context)


@csrf_protect
def signin(request):
    if 'id' in request.session:
        id_per = int(request.session['id'])
        user = User.objects.get(id=id_per)
        return redirect('/')
    if request.method == 'POST':
        INform = SignInForm(request.POST)
        print(INform)
        if INform.is_valid():
            cd = INform.cleaned_data
            print(cd)
            try:
                usr_account = User.objects.get(email=cd["email"])
            except User.DoesNotExist:
                print("Error: user does not exist")
                return redirect('/')
            if(usr_account.password == cd["password"]):
                id_usr = int(usr_account.id)
                request.session.set_expiry(24*3600)
                request.session['id'] = id_usr
                response = redirect(f'/')
                return response
            else:
                print("Error: wrong password")

        else:
            print("Error: Non Valid Form")
    else:
        INform = SignInForm()
        print("SENT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    return redirect('/')


@csrf_protect
def signup(request):
    if 'id' in request.session:
        id_per = int(request.session['id'])
        user = User.objects.get(id=id_per)
        return redirect('/')
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            try:
                form.save()
                return redirect('/')
            except :
                form.add_error(None, "error add post")

        else:
            print("Error: Non Valid Form")
    else:
        form = SignUpForm()
        print("SENT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    return redirect('/')

@csrf_protect
def addalbum(request):
    if 'id' in request.session:
        id_per = int(request.session['id'])
        user = User.objects.get(id=id_per)
    else:
        return redirect('/')
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data["name"]
            description = form.cleaned_data["description"]
            resize = form.cleaned_data["resize"]
            try:
                alb = Album(name=name, description=description, resize=resize, author=user)
                alb.save()
                return redirect('/user/')
            except :
                form.add_error(None, "error add post")

        else:
            print("Error: Non Valid Form")

    return redirect('/user/')


@csrf_protect
def addphoto(request, pk):
    print("I`m in", pk)
    if 'id' in request.session:
        id_per = int(request.session['id'])
        user = User.objects.get(id=id_per)
    else:
        return redirect('/')
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        album = Album.objects.get(id=pk)
        if form.is_valid():
            name = form.cleaned_data["name"]
            original = form.cleaned_data["original"]
            print(name, original, album)
            try:
                photo = Photo(name=name, original=original, album_set=album)
                photo.save()
                return redirect('/user/')
            except :
                form.add_error(None, "error add post")

        else:
            print("Error: Non Valid Form")

    return redirect('/album/'+pk+"/")