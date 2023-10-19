from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'base/home.html')

def contest(request):
    return render(request, 'base/contest-details.html')

def categories(request):
    return render(request, 'base/categories.html')


def user(request):
    return render(request, 'base/users.html')


def contests(request):
    return render(request, 'base/contests.html')