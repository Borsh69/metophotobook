from django.urls import path
from . import views 

urlpatterns = [
    
    path('', views.home, name="home"),
    path('contest/', views.contest, name="contest"),
    path('categories/', views.categories, name="categories"),
    path('user/', views.user, name="user"),
    path('contests/', views.contests, name="contests"),
    path('signin/', views.signin, name="signin"),
    
]