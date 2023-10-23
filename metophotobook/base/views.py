from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    photo = Photo.objects.filter(isopen=True)
    popul_photo = photo.order_by('-popularity')[:5]
    user = User.objects.all()
    close_photo = Photo.objects.filter(isopen=False)
    context = {'close_photo': close_photo,'photo_popul': popul_photo, 'user': user}
    return render(request, 'base/home.html', context)

def contest(request):
    return render(request, 'base/contest-details.html')

def categories(request):
    return render(request, 'base/categories.html')


def user(request):
    return render(request, 'base/users.html')


def contests(request):
    return render(request, 'base/contests.html')