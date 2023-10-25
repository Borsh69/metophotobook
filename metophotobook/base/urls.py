from django.urls import path
from . import views 

urlpatterns = [
    
    path('', views.home, name="home"),
    path('contest/', views.contest, name="contest"),
    path('albums/', views.albums, name="albums"),
    path('user/', views.user, name="user"),
    path('contests/', views.contests, name="contests"),
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('album/<str:pk>/', views.album, name="album"),
]