from django.urls import path, include
from . import views

urlpatterns = [
    path('reg/',views.reg, name='reg'),
    path('log/',views.login, name='login'),
    path('profile/',views.profile, name='profile'),
    path('logout/', views.logoutPage,name='logout'),
]