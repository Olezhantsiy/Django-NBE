from django.urls import path
from .views import TestDetailView
from . import views

urlpatterns = [
    path('test/<int:typeq>/', views.TestDetailView.as_view(), name= 'testq'),
    path('', views.TestPageView.as_view(), name='testmanager'),
    #path('test1/', views.test1, name='test1'),
    path('test2/', views.test2, name='test2'),
]
